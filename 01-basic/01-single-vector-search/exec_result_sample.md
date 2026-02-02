```json
(.venv) PS C:\> python app.py
Deleted 63 documents
Uploaded 63 documents
検索クエリを入力してください（終了するには空行でEnter）
> LLMとRAGの関係を教えてください
total count of search results=50

search results(output only top 5):
 [
  {
    "id": "1",
    "content": "RAG では検索結果を LLM の入力として使います。",
    "@search.score": 0.7709117,
    "@search.reranker_score": null,
    "@search.highlights": null,
    "@search.captions": null,
    "@search.document_debug_info": null,
    "@search.reranker_boosted_score": null
  },
  {
    "id": "25",
    "content": "スコアの高い文書だけをLLMに渡すことが重要です。",
    "@search.score": 0.6616588,
    "@search.reranker_score": null,
    "@search.highlights": null,
    "@search.captions": null,
    "@search.document_debug_info": null,
    "@search.reranker_boosted_score": null
  },
  {
    "id": "26",
    "content": "RAGは社内文書検索によく使われます。",
    "@search.score": 0.6592641,
    "@search.reranker_score": null,
    "@search.highlights": null,
    "@search.captions": null,
    "@search.document_debug_info": null,
    "@search.reranker_boosted_score": null
  },
  {
    "id": "27",
    "content": "GraphRAGは関係性をグラフとして扱います。",
    "@search.score": 0.64964247,
    "@search.reranker_score": null,
    "@search.highlights": null,
    "@search.captions": null,
    "@search.document_debug_info": null,
    "@search.reranker_boosted_score": null
  },
  {
    "id": "23",
    "content": "RAGは幻覚を減らすための実践的なアプローチです。",
    "@search.score": 0.64413375,
    "@search.reranker_score": null,
    "@search.highlights": null,
    "@search.captions": null,
    "@search.document_debug_info": null,
    "@search.reranker_boosted_score": null
  }
]

=== Answer ===
LLM（大規模言語モデル）とRAG（Retrieval Augmented Generation）は、密接に関連した技術です。RAGは、検索結果をLLMの入力として利用する手法であり、スコアの高い文書をLLMに渡すことが重要です。この手法によって生成された結果の品質は、RAGの検索精度によって大きく影響を受けます。また、RAGは社内文書検索に用いられ、幻覚を減らすための実践的なアプローチでもあります。さらに、RAGのプロンプト設計やベクトル検索などの要素も、システム全体の品質に寄与します。
> 滋賀県と京都府ではどちらの人口が多いですか
total count of search results=50

search results(output only top 5):
 [
  {
    "id": "57",
    "content": "滋賀県の県庁所在地は大津市で、面積は約4千平方キロメートル、人口は約140万人、名物は鮒ずしです。",
    "@search.score": 0.70384735,
    "@search.reranker_score": null,
    "@search.highlights": null,
    "@search.captions": null,
    "@search.document_debug_info": null,
    "@search.reranker_boosted_score": null
  },
  {
    "id": "58",
    "content": "京都府の府庁所在地は京都市で、面積は約4千6百平方キロメートル、人口は約255万人、名物は湯豆腐です。",
    "@search.score": 0.66285956,
    "@search.reranker_score": null,
    "@search.highlights": null,
    "@search.captions": null,
    "@search.document_debug_info": null,
    "@search.reranker_boosted_score": null
  },
  {
    "id": "46",
    "content": "神奈川県の県庁所在地は横浜市で、面積は約2千4百平方キロメートル、人口は約920万人、名物は崎陽軒のシウマイです。",
    "@search.score": 0.6556459,
    "@search.reranker_score": null,
    "@search.highlights": null,
    "@search.captions": null,
    "@search.document_debug_info": null,
    "@search.reranker_boosted_score": null
  },
  {
    "id": "61",
    "content": "奈良県の県庁所在地は奈良市で、面積は約3千7百平方キロメートル、人口は約130万人、名物は柿の葉寿司です。",
    "@search.score": 0.64898527,
    "@search.reranker_score": null,
    "@search.highlights": null,
    "@search.captions": null,
    "@search.document_debug_info": null,
    "@search.reranker_boosted_score": null
  },
  {
    "id": "43",
    "content": "埼玉県の県庁所在地はさいたま市で、面積は約3千8百平方キロメートル、人口は約730万人、名物は草加せんべいです。",
    "@search.score": 0.64200443,
    "@search.reranker_score": null,
    "@search.highlights": null,
    "@search.captions": null,
    "@search.document_debug_info": null,
    "@search.reranker_boosted_score": null
  }
]

=== Answer ===
京都府の人口が約255万人で、滋賀県の人口が約140万人ですので、京都府の方が多いです。
>
終了します。
(.venv) PS C:\> 
```