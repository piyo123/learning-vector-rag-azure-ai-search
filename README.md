# Azure AI Search を使った Vector RAG の学習

## 1. Basic (Classic)

00-assets に格納した documents.txt を読み込み、1行を1チャンクとして解析しIndex にベクトルデータ（Embeddings）を格納します。その後、ユーザーが入力したクエリをもとに Index を検索し、LLM へ結果を渡して最終回答を生成します。

- `01-single-vector-search`: Vector Search のみを使用したバージョンです
- `02-hybrid-search`: Vector Search + Keyword Search を使用したバージョンです
- `03-semantic-hybrid-search`: 簡単のため今回はメタデータを Index に持たせていませんが、content だけでも、チャンクの意味理解、クエリとドキュメントの文脈的な関連性を評価し、意味的な類似性で semantic_reranker 値を算出し結果を並び替えます。

本例では Index 自体は Azure Portal で作成しました。  
`01-single-vector-search` および `02-hybrid-search` は `kazuma-rag-index1-initial.json` を、`03-semantic-hybrid-search` は `kazuma-rag-index1-semantic.json` を参照してください。

## 2. Agentic Retrieval (Public Preview as of Feb. 2, 2026)

[Agentic retrieval in Azure AI Search](agentic_retrieval_overview) によると Agentic Retrieval とは次のようなことを指すようです。

> - 大規模言語モデル（LLM）を使用して、複雑なクエリをより小さく、焦点を絞ったサブクエリ> に分解し、インデックス化されたコンテンツ全体をより網羅的に検索します。サブクエリに> は、追加の文脈としてチャット履歴を含めることもできます。
>
> - サブクエリは並列で実行されます。各サブクエリは意味的に再ランキングされ、最も関連性> の高い一致結果が優先されます。
>
> - 最良の検索結果を統合し、LLM が独自コンテンツを用いて回答を生成できる単一のレスポンス>としてまとめます。
> 
> - このレスポンスはモジュール化されていながら包括的で、クエリプランや参照元ドキュメントも含まれます。検索結果のみを> グラウンディングデータとして利用することも、LLM を呼び出して回答文を生成することも選択できます。

本リポジトリでは、[Quickstart: Agentic retrieval](qs_agentic_retrieval) をベースに、Azure Blob Storage に格納した `stories.pdf` (00-assetsにもコピーが入っています) をデータソースとして Agentic Retrieval を学習しました。

### 2.1. Concept and Relationships (My understanding)
```
    Knowledge Base
    ┃
    ┣ Knowledge source 1
    ┃	┣ データソース: Azure Blob, Cosmos DB, SQL Database, SharePoint 等
    ┃	┣ インデックス: embeddings(vector) とメタデータを格納した検索対象
    ┃	┣ インデクサー: Embeddingしインデックスに格納。スケジュール実行、差分更新も可能。スキルを使用する。
    ┃	┗ スキルセット: インデクサーが使用するスキルをまとめたもの。※2026/1/24現在、Azure PortalでもJSONを書かないといけない。
    ┃		┣ テキスト処理系
    ┃       ┃	┣ Text Split Skill: チャンキング戦略を定義。長文を分割し他のスキルのインプットとする役割も担う。
    ┃       ┃	┣ Text Merge: 複数のフィールドや分割されたテキストを一つにまとめる。OCR や画像解析後のテキスト統合に利用。
    ┃       ┃	┣ Conditional: 条件に基づいて値を設定したり、データをフィルタリングする。
    ┃       ┃	┣ Shaper: 複数のフィールドを組み合わせて複雑な型を作成する。（例：住所や氏名の構造化）
    ┃		┣ 言語・テキスト解析系
    ┃       ┃	┣ Language Detection: テキストの言語を判定し、言語コードを出力
    ┃       ┃	┣ Key Phrase Extraction: 重要なキーフレーズを抽出
    ┃       ┃	┣ Sentiment Analysis: テキストの感情（ポジティブ、ネガティブ、中立）を分析
    ┃       ┃	┣ Entity Recognition: 人名、組織名、場所などのエンティティを抽出
    ┃		┣ 画像・ドキュメント解析系
    ┃       ┃	┣ OCR: 画像内の文字を認識してテキスト化
    ┃       ┃	┣ Document Extraction: ドキュメントからテキストや画像を抽出
    ┃       ┃	┣ Document Layout / Content Understanding: レイアウト情報や構造化データを抽出（高度なドキュメント解析用）
    ┃		・
    ┃		・
    ┃		・　
    ┣ Knowledge source 2
    ・
    ・
    ・
```

### 2.2 問題発生
Indexer を実行しても、Embeddings が Index に格納されない事象が発生しました。  
一言でいうと課題は Embeddings 生成時の **Double型からSingle型への型不一致** です。

> Azure Searchの `AzureOpenAIEmbeddingSkill` をインデックス時のベクトル化に使用する場合：
> - スキルはJSON配列として埋め込みを返す（`Collection(Edm.Double)` としてシリアライズされる）
> - Azure Searchのベクトルフィールドは `Collection(Edm.Single)` または他の特定の型を要求する
> - エンリッチメント時にDouble→Singleへ自動変換する組み込み機能が存在しない
> 
> **発生したエラー:**
> ```
> The data field 'page_embeddings' has an invalid value of type 'Collection(Edm.Double)'. 
> The expected type was 'Collection(Edm.Single)'.
> ```
> 
> **他のスキルは動いていたのか:**  
> SplitSkill(テキスト分割)、WebApiSkill（タイトル抽出）は正常動作していた。  
> Embeddingsのみが型変換エラーで失敗した。

GitHub Copilot も解を見いだせなかったため、Index に Embeddings やメタデータなどをアップロードする処理は別に作成するという Copilot のアドバイスに従い、別処理としました。


### 2.3 出力の説明
- `response_contents`: 取得したドキュメントを引用しながら、クエリに対する統合された LLM 生成の回答を提供します。 回答の統合生成が有効になっていない場合、このセクションにはドキュメントから直接抽出されたコンテンツが表示されます。
- `activity_contents` : 検索プロセス中に実行された手順を記録します。これには、回答生成用 LLM のデプロイメントによって生成されたサブクエリや、セマンティック ランキング、クエリ計画、回答生成に使用されたトークンが含まれます。
- `references_contents`: 応答に貢献したドキュメントが一覧表示されます。各ドキュメントは、 doc_keyによって識別されます。（最初の5件のみ表示）


## 3. Refrences
- [What is Azure AI Search?](what_is_rag_in_azure_ai_search)
- [Classic RAG pattern for Azure AI Search](what_is_classic_search)
- [Readme for classic RAG in Azure AI Search](classic_github_repo)
- [Agentic retrieval in Azure AI Search](agentic_retrieval_overview)
- [Modern RAG with agentic retrieval](what_is_agentic_retrieval)
- [Retrieval-augmented Generation (RAG) in Azure AI Search](what_is_rag_in_azure_ai_search)
- [Azure SDK For Python (Preview) References](azure_sdk_python_pre_reference)
- [Skills for extra processing during indexing (Azure AI Search)](indexing_skills)
- [Quickstart: Agentic retrieval](qs_agentic_retrieval)


## 4. 備忘録

> [!NOTE]
> TODO  
> [Create an indexed SharePoint knowledge source][agentic_sharepoint]
> 2026.01.24 現在、Azure Portal から SPO のデータソースは作れないため、上記ドキュメントを参照しプログラムで作成する。[^1]

[^1]:Azure AI Search は、Microsoft Foundry における `プロジェクト` 内で作成する `エージェント`([Foundry Agent Service][foundry_agent_service]) のナレッジを司る `Foundry IQ` の構成要素の１つとなり、Azure AI Search 内では SPO のデータソースを作れないが、Foundry IQ からは SPO のデータソース作成のUIもある。今後は KB 自体も Foundry 内で作るようになっていくのだろう。



[waht_is_azure_ai_search]: https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search

[what_is_rag_in_azure_ai_search]: https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview?tabs=videos

[what_is_classic_search]: https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview?tabs=videos#classic-rag-pattern-for-azure-ai-search

[what_is_agentic_retrieval]: https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search?tabs=indexing%2Cquickstarts#what-is-agentic-retrieval

[agentic_retrieval_overview]: https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview

[azure_sdk_python_pre_reference]: https://learn.microsoft.com/ja-jp/python/api/azure-search-documents/azure.search.documents.models.vectorizedquery?view=azure-python-preview

[classic_github_repo]: https://github.com/Azure-Samples/azure-search-classic-rag/blob/main/README.md

[qs_agentic_retrieval]: https://learn.microsoft.com/en-us/azure/search/search-get-started-agentic-retrieval?tabs=foundry&pivots=programming-language-python

[indexing_skills]: https://learn.microsoft.com/en-us/azure/search/cognitive-search-predefined-skills

[agentic_sharepoint]: https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-sharepoint-indexed?pivots=python

[foundry_agent_service]: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview?view=foundry&preserve-view=true