```json
(.venv) PS C:\> python 4-search.py
検索クエリを入力してください（終了するには空行でEnter）
> 桃太郎は何をしましたか
Retrieved content from 'stories-index-knowledge-base' successfully.

*** response_content:
桃太郎は、村を荒らす鬼を退治するために旅に出ました。道中で犬、猿、きじと出会い、仲間を増やし、力を合わせて鬼ヶ島に乗り込み、見事に鬼を退治して宝物を持って村へ帰り、みんなを幸せにしました。[ref_id:0]


*** activity_content:
[
  {
    "id": 0,
    "type": "modelQueryPlanning",
    "elapsed_ms": 1456,
    "input_tokens": 1453,
    "output_tokens": 63
  },
  {
    "id": 1,
    "type": "searchIndex",
    "elapsed_ms": 715,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:38:09.943Z",
    "count": 8,
    "search_index_arguments": {
      "search": "桃太郎の物語",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 2,
    "type": "searchIndex",
    "elapsed_ms": 567,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:38:10.519Z",
    "count": 8,
    "search_index_arguments": {
      "search": "桃太郎の冒険",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 3,
    "type": "searchIndex",
    "elapsed_ms": 594,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:38:11.114Z",
    "count": 7,
    "search_index_arguments": {
      "search": "桃太郎の行動",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 4,
    "type": "agenticReasoning",
    "reasoning_tokens": 5931,
    "retrieval_reasoning_effort": {
      "kind": "low"
    }
  },
  {
    "id": 5,
    "type": "modelAnswerSynthesis",
    "elapsed_ms": 2251,
    "input_tokens": 5127,
    "output_tokens": 98
  }
]


*** references_content:
[
  {
    "type": "searchIndex",
    "id": "0",
    "activity_source": 1,
    "source_data": {
      "id": "doc1",
      "page_chunk": "桃太郎 \nむかしむかし、川上から大きな桃がどんぶらこと流れてきました。洗濯をしてい\nたおばあさんは、その桃を家に持ち帰り、おじいさんと分けようとしました。とこ\nろが桃を割ると、中から元気な男の子が飛び出してきました。二人は大喜\nびでその子を桃太郎と名づけ、大切に育てました。やがて桃太郎は、村を荒\nらす⿁を退治するため旅に出ます。道中で犬、猿、きじと出会い、きびだん\nごを分け与えて仲間にしました。力を合わせて⿁ヶ島に乗り込み、見事⿁を\n退治した桃太郎は、宝物を持って村へ帰り、みんなを幸せにしました。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.815988,
    "doc_key": "doc1"
  },
  {
    "type": "searchIndex",
    "id": "3",
    "activity_source": 1,
    "source_data": {
      "id": "doc10",
      "page_chunk": "親指姫 \n花の中から生まれた親指ほどの小さな女の子は、親指姫と名づけられまし\nた。ある夜、がまがえるにさらわれ、望まぬ結婚を迫られますが、親切な魚や\nつばめに助けられます。⾧い旅の末、花の国にたどり着いた親指姫は、自分\nと同じ大きさの王子と出会いました。二人は心を通わせ、幸せに暮らしま\nす。親指姫は、自分の居場所を探し続けた末に、本当に安心できる世界\nを見つけたのです。 \n ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.3734334,
    "doc_key": "doc10"
  },
  {
    "type": "searchIndex",
    "id": "6",
    "activity_source": 1,
    "source_data": {
      "id": "doc9",
      "page_chunk": "鶴の恩返し \nむかし、貧しい男が罠にかかった鶴を助けてあげました。数日後、その男の家\nに美しい女性が訪れ、妻となります。彼女は機織りをして立派な布を織り、\n「決して中をのぞかないでください」と言いました。男は約束を破り、こっそり中\nをのぞいてしまいます。そこには、自分の羽を抜いて布を織る鶴の姿がありま\nした。正体を知られた鶴は、悲しそうに空へ飛び立ちます。男は深く後悔し\nましたが、鶴の優しさは心に残り続けました。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.177589,
    "doc_key": "doc9"
  },
  {
    "type": "searchIndex",
    "id": "1",
    "activity_source": 2,
    "source_data": {
      "id": "doc6",
      "page_chunk": "醜いアヒルの子 \nある農場で生まれたアヒルの子は、他の子と違って大きく、見た目も冴えま\nせんでした。そのため仲間や周囲から笑われ、ひとりぼっちで過ごします。つら\nさに耐えきれず旅に出たアヒルの子は、寒い冬を必死に生き延びました。春\nになり湖に映った自分の姿を見ると、そこには美しい白鳥がいました。実はそ\nの子は白鳥だったのです。⾧い苦しみを経て、本来の自分に出会えたアヒル\nの子は、堂々と空を羽ばたきました。この物語は、自分の価値はすぐには分\nからないことを教えてくれます。 \n ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.1307106,
    "doc_key": "doc6"
  },
  {
    "type": "searchIndex",
    "id": "8",
    "activity_source": 1,
    "source_data": {
      "id": "doc8",
      "page_chunk": "マッチ売りの少女 \n寒い大晦日の夜、裸足の少女がマッチを売り歩いていました。誰も買ってく\nれず、帰る家もありません。凍えながらマッチを一本擦ると、暖かいストーブや\nごちそう、優しいおばあさんの幻が見えました。少女は次々とマッチを擦り、\n幸せな光景に包まれます。やがて朝になると、少女は静かに雪の中で眠って\nいました。人々は気づきませんでしたが、少女の心は温かい夢に満ちていま\nした。この物語は、弱い立場の人への思いやりを私たちに問いかけます。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.0799327,
    "doc_key": "doc8"
  }
]

> 桃太郎のお供は誰ですか
Retrieved content from 'stories-index-knowledge-base' successfully.

*** response_content:
桃太郎のお供は犬、猿、きじです。彼らは桃太郎と共に力を合わせて鬼ヶ島に乗り込みました[ref_id:0]。


*** activity_content:
[
  {
    "id": 0,
    "type": "modelQueryPlanning",
    "elapsed_ms": 1466,
    "input_tokens": 1454,
    "output_tokens": 68
  },
  {
    "id": 1,
    "type": "searchIndex",
    "elapsed_ms": 993,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:41:07.597Z",
    "count": 8,
    "search_index_arguments": {
      "search": "桃太郎の物語",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 2,
    "type": "searchIndex",
    "elapsed_ms": 564,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:41:08.171Z",
    "count": 3,
    "search_index_arguments": {
      "search": "桃太郎のお供のキャラクター",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 3,
    "type": "searchIndex",
    "elapsed_ms": 574,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:41:08.746Z",
    "count": 2,
    "search_index_arguments": {
      "search": "桃太郎の仲間について",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 4,
    "type": "agenticReasoning",
    "reasoning_tokens": 5931,
    "retrieval_reasoning_effort": {
      "kind": "low"
    }
  },
  {
    "id": 5,
    "type": "modelAnswerSynthesis",
    "elapsed_ms": 1042,
    "input_tokens": 4660,
    "output_tokens": 54
  }
]


*** references_content:
[
  {
    "type": "searchIndex",
    "id": "0",
    "activity_source": 1,
    "source_data": {
      "id": "doc1",
      "page_chunk": "桃太郎 \nむかしむかし、川上から大きな桃がどんぶらこと流れてきました。洗濯をしてい\nたおばあさんは、その桃を家に持ち帰り、おじいさんと分けようとしました。とこ\nろが桃を割ると、中から元気な男の子が飛び出してきました。二人は大喜\nびでその子を桃太郎と名づけ、大切に育てました。やがて桃太郎は、村を荒\nらす⿁を退治するため旅に出ます。道中で犬、猿、きじと出会い、きびだん\nごを分け与えて仲間にしました。力を合わせて⿁ヶ島に乗り込み、見事⿁を\n退治した桃太郎は、宝物を持って村へ帰り、みんなを幸せにしました。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.815988,
    "doc_key": "doc1"
  },
  {
    "type": "searchIndex",
    "id": "1",
    "activity_source": 1,
    "source_data": {
      "id": "doc10",
      "page_chunk": "親指姫 \n花の中から生まれた親指ほどの小さな女の子は、親指姫と名づけられまし\nた。ある夜、がまがえるにさらわれ、望まぬ結婚を迫られますが、親切な魚や\nつばめに助けられます。⾧い旅の末、花の国にたどり着いた親指姫は、自分\nと同じ大きさの王子と出会いました。二人は心を通わせ、幸せに暮らしま\nす。親指姫は、自分の居場所を探し続けた末に、本当に安心できる世界\nを見つけたのです。 \n ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.3734334,
    "doc_key": "doc10"
  },
  {
    "type": "searchIndex",
    "id": "2",
    "activity_source": 1,
    "source_data": {
      "id": "doc9",
      "page_chunk": "鶴の恩返し \nむかし、貧しい男が罠にかかった鶴を助けてあげました。数日後、その男の家\nに美しい女性が訪れ、妻となります。彼女は機織りをして立派な布を織り、\n「決して中をのぞかないでください」と言いました。男は約束を破り、こっそり中\nをのぞいてしまいます。そこには、自分の羽を抜いて布を織る鶴の姿がありま\nした。正体を知られた鶴は、悲しそうに空へ飛び立ちます。男は深く後悔し\nましたが、鶴の優しさは心に残り続けました。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.177589,
    "doc_key": "doc9"
  },
  {
    "type": "searchIndex",
    "id": "3",
    "activity_source": 1,
    "source_data": {
      "id": "doc8",
      "page_chunk": "マッチ売りの少女 \n寒い大晦日の夜、裸足の少女がマッチを売り歩いていました。誰も買ってく\nれず、帰る家もありません。凍えながらマッチを一本擦ると、暖かいストーブや\nごちそう、優しいおばあさんの幻が見えました。少女は次々とマッチを擦り、\n幸せな光景に包まれます。やがて朝になると、少女は静かに雪の中で眠って\nいました。人々は気づきませんでしたが、少女の心は温かい夢に満ちていま\nした。この物語は、弱い立場の人への思いやりを私たちに問いかけます。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.0799327,
    "doc_key": "doc8"
  },
  {
    "type": "searchIndex",
    "id": "4",
    "activity_source": 1,
    "source_data": {
      "id": "doc6",
      "page_chunk": "醜いアヒルの子 \nある農場で生まれたアヒルの子は、他の子と違って大きく、見た目も冴えま\nせんでした。そのため仲間や周囲から笑われ、ひとりぼっちで過ごします。つら\nさに耐えきれず旅に出たアヒルの子は、寒い冬を必死に生き延びました。春\nになり湖に映った自分の姿を見ると、そこには美しい白鳥がいました。実はそ\nの子は白鳥だったのです。⾧い苦しみを経て、本来の自分に出会えたアヒル\nの子は、堂々と空を羽ばたきました。この物語は、自分の価値はすぐには分\nからないことを教えてくれます。 \n ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.0749702,
    "doc_key": "doc6"
  }
]

> 鬼が出てくるお話を教えてください
Retrieved content from 'stories-index-knowledge-base' successfully.

*** response_content:
鬼が出てくるお話としては、桃太郎の物語があります。桃太郎は、村を荒らす鬼を退治するために旅に出て、仲間と共に鬼ヶ島に乗り込み、見事に鬼を退治して宝物を持って村へ帰ります [ref_id:0]。


*** activity_content:
[
  {
    "id": 0,
    "type": "modelQueryPlanning",
    "elapsed_ms": 1316,
    "input_tokens": 1457,
    "output_tokens": 73
  },
  {
    "id": 1,
    "type": "searchIndex",
    "elapsed_ms": 663,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:41:52.919Z",
    "count": 5,
    "search_index_arguments": {
      "search": "鬼が出てくるお話",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 2,
    "type": "searchIndex",
    "elapsed_ms": 560,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:41:53.480Z",
    "count": 4,
    "search_index_arguments": {
      "search": "日本の鬼に関する伝説",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 3,
    "type": "searchIndex",
    "elapsed_ms": 591,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:41:54.072Z",
    "count": 5,
    "search_index_arguments": {
      "search": "鬼が登場する物語",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 4,
    "type": "agenticReasoning",
    "reasoning_tokens": 5931,
    "retrieval_reasoning_effort": {
      "kind": "low"
    }
  },
  {
    "id": 5,
    "type": "modelAnswerSynthesis",
    "elapsed_ms": 1217,
    "input_tokens": 4207,
    "output_tokens": 89
  }
]


*** references_content:
[
  {
    "type": "searchIndex",
    "id": "0",
    "activity_source": 1,
    "source_data": {
      "id": "doc1",
      "page_chunk": "桃太郎 \nむかしむかし、川上から大きな桃がどんぶらこと流れてきました。洗濯をしてい\nたおばあさんは、その桃を家に持ち帰り、おじいさんと分けようとしました。とこ\nろが桃を割ると、中から元気な男の子が飛び出してきました。二人は大喜\nびでその子を桃太郎と名づけ、大切に育てました。やがて桃太郎は、村を荒\nらす⿁を退治するため旅に出ます。道中で犬、猿、きじと出会い、きびだん\nごを分け与えて仲間にしました。力を合わせて⿁ヶ島に乗り込み、見事⿁を\n退治した桃太郎は、宝物を持って村へ帰り、みんなを幸せにしました。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.3688252,
    "doc_key": "doc1"
  },
  {
    "type": "searchIndex",
    "id": "3",
    "activity_source": 1,
    "source_data": {
      "id": "doc7",
      "page_chunk": "赤ずきん \n赤いずきんをかぶった女の子は、おばあさんの家へお見舞いに行く途中でし\nた。森の中で出会ったおおかみは、やさしいふりをして道を聞き出します。おお\nかみは先回りしておばあさんを食べ、赤ずきんを待ち構えました。違和感を\n覚えつつも近づいた赤ずきんは、ついにおおかみに食べられてしまいます。しか\nし、通りかかった狩人が気づき、おおかみのお腹から二人を助け出しました。\n赤ずきんは人を簡単に信じないことの大切さを学び、無事に家へ帰りまし\nた。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.297577,
    "doc_key": "doc7"
  },
  {
    "type": "searchIndex",
    "id": "4",
    "activity_source": 1,
    "source_data": {
      "id": "doc8",
      "page_chunk": "マッチ売りの少女 \n寒い大晦日の夜、裸足の少女がマッチを売り歩いていました。誰も買ってく\nれず、帰る家もありません。凍えながらマッチを一本擦ると、暖かいストーブや\nごちそう、優しいおばあさんの幻が見えました。少女は次々とマッチを擦り、\n幸せな光景に包まれます。やがて朝になると、少女は静かに雪の中で眠って\nいました。人々は気づきませんでしたが、少女の心は温かい夢に満ちていま\nした。この物語は、弱い立場の人への思いやりを私たちに問いかけます。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.206146,
    "doc_key": "doc8"
  },
  {
    "type": "searchIndex",
    "id": "1",
    "activity_source": 2,
    "source_data": {
      "id": "doc2",
      "page_chunk": "浦島太郎 \nむかし、浦島太郎という心やさしい若者がいました。ある日、子どもたちにい\nじめられている亀を助けてあげました。すると数日後、その亀が現れ、海の底\nの竜宮城へ案内してくれました。そこでは美しい乙姫が出迎え、浦島太郎\nは夢のような日々を過ごします。しかし村のことが気になり、帰ることにしまし\nた。別れ際、乙姫から玉手箱を渡され、「決して開けてはいけません」と言わ\nれます。地上に戻ると、村の様子はすっかり変わり、知っている人は誰もいま\nせんでした。驚いた浦島太郎が玉手箱を開けると、白い煙が立ちのぼり、た\nちまち老人になってしまいました。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.1050558,
    "doc_key": "doc2"
  },
  {
    "type": "searchIndex",
    "id": "5",
    "activity_source": 1,
    "source_data": {
      "id": "doc3",
      "page_chunk": "さるかに合戦 \nむかし、正直なかにと、ずる賢いさるがいました。ある日、さるはかにに「この柿\nの種と、おにぎりを交換しよう」と持ちかけます。かには承知し、種を植えて大\n切に育てました。やがて柿は立派に実りますが、木に登れないかには取るこ\nとができません。そこへさるが現れ、熟していない柿を投げつけ、かにを傷つけ\nてしまいました。怒ったかにの仲間たちは、臼や栗、蜂と力を合わせ、さるに\n仕返しをします。最後にさるは自分の過ちを認め、深く反省しました。この話\nは、ずるをすると必ず報いがあることを教えています。 \n ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 1.9728831,
    "doc_key": "doc3"
  }
]

> サルが出てくるお話を教えてください
Retrieved content from 'stories-index-knowledge-base' successfully.

*** response_content:
サルが出てくるお話は「さるかに合戦」です。この話では、正直なかにとずる賢いさるが登場し、最終的にサルは自分の過ちを認め、反省します [ref_id:0]。


*** activity_content:
[
  {
    "id": 0,
    "type": "modelQueryPlanning",
    "elapsed_ms": 1378,
    "input_tokens": 1458,
    "output_tokens": 72
  },
  {
    "id": 1,
    "type": "searchIndex",
    "elapsed_ms": 593,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:42:17.715Z",
    "count": 7,
    "search_index_arguments": {
      "search": "サルが出てくるお話の例",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 2,
    "type": "searchIndex",
    "elapsed_ms": 593,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:42:18.310Z",
    "count": 4,
    "search_index_arguments": {
      "search": "サルが登場する物語",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 3,
    "type": "searchIndex",
    "elapsed_ms": 573,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:42:18.883Z",
    "count": 4,
    "search_index_arguments": {
      "search": "サルに関する童話",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 4,
    "type": "agenticReasoning",
    "reasoning_tokens": 5931,
    "retrieval_reasoning_effort": {
      "kind": "low"
    }
  },
  {
    "id": 5,
    "type": "modelAnswerSynthesis",
    "elapsed_ms": 1057,
    "input_tokens": 4402,
    "output_tokens": 77
  }
]


*** references_content:
[
  {
    "type": "searchIndex",
    "id": "0",
    "activity_source": 1,
    "source_data": {
      "id": "doc3",
      "page_chunk": "さるかに合戦 \nむかし、正直なかにと、ずる賢いさるがいました。ある日、さるはかにに「この柿\nの種と、おにぎりを交換しよう」と持ちかけます。かには承知し、種を植えて大\n切に育てました。やがて柿は立派に実りますが、木に登れないかには取るこ\nとができません。そこへさるが現れ、熟していない柿を投げつけ、かにを傷つけ\nてしまいました。怒ったかにの仲間たちは、臼や栗、蜂と力を合わせ、さるに\n仕返しをします。最後にさるは自分の過ちを認め、深く反省しました。この話\nは、ずるをすると必ず報いがあることを教えています。 \n ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.7649443,
    "doc_key": "doc3"
  },
  {
    "type": "searchIndex",
    "id": "1",
    "activity_source": 3,
    "source_data": {
      "id": "doc9",
      "page_chunk": "鶴の恩返し \nむかし、貧しい男が罠にかかった鶴を助けてあげました。数日後、その男の家\nに美しい女性が訪れ、妻となります。彼女は機織りをして立派な布を織り、\n「決して中をのぞかないでください」と言いました。男は約束を破り、こっそり中\nをのぞいてしまいます。そこには、自分の羽を抜いて布を織る鶴の姿がありま\nした。正体を知られた鶴は、悲しそうに空へ飛び立ちます。男は深く後悔し\nましたが、鶴の優しさは心に残り続けました。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.466304,
    "doc_key": "doc9"
  },
  {
    "type": "searchIndex",
    "id": "2",
    "activity_source": 3,
    "source_data": {
      "id": "doc1",
      "page_chunk": "桃太郎 \nむかしむかし、川上から大きな桃がどんぶらこと流れてきました。洗濯をしてい\nたおばあさんは、その桃を家に持ち帰り、おじいさんと分けようとしました。とこ\nろが桃を割ると、中から元気な男の子が飛び出してきました。二人は大喜\nびでその子を桃太郎と名づけ、大切に育てました。やがて桃太郎は、村を荒\nらす⿁を退治するため旅に出ます。道中で犬、猿、きじと出会い、きびだん\nごを分け与えて仲間にしました。力を合わせて⿁ヶ島に乗り込み、見事⿁を\n退治した桃太郎は、宝物を持って村へ帰り、みんなを幸せにしました。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.2261512,
    "doc_key": "doc1"
  },
  {
    "type": "searchIndex",
    "id": "3",
    "activity_source": 1,
    "source_data": {
      "id": "doc10",
      "page_chunk": "親指姫 \n花の中から生まれた親指ほどの小さな女の子は、親指姫と名づけられまし\nた。ある夜、がまがえるにさらわれ、望まぬ結婚を迫られますが、親切な魚や\nつばめに助けられます。⾧い旅の末、花の国にたどり着いた親指姫は、自分\nと同じ大きさの王子と出会いました。二人は心を通わせ、幸せに暮らしま\nす。親指姫は、自分の居場所を探し続けた末に、本当に安心できる世界\nを見つけたのです。 \n ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.1404362,
    "doc_key": "doc10"
  },
  {
    "type": "searchIndex",
    "id": "4",
    "activity_source": 1,
    "source_data": {
      "id": "doc8",
      "page_chunk": "マッチ売りの少女 \n寒い大晦日の夜、裸足の少女がマッチを売り歩いていました。誰も買ってく\nれず、帰る家もありません。凍えながらマッチを一本擦ると、暖かいストーブや\nごちそう、優しいおばあさんの幻が見えました。少女は次々とマッチを擦り、\n幸せな光景に包まれます。やがて朝になると、少女は静かに雪の中で眠って\nいました。人々は気づきませんでしたが、少女の心は温かい夢に満ちていま\nした。この物語は、弱い立場の人への思いやりを私たちに問いかけます。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.0462582,
    "doc_key": "doc8"
  }
]

> おばあさんが出てくるのはどのお話ですか
Retrieved content from 'stories-index-knowledge-base' successfully.

*** response_content:
おばあさんが出てくるお話には、「赤ずきん」があります。この物語では、赤ずきんが森でおおかみと出会い、おばあさんの家に向かう途中で危険に遭遇しますが、最終的に狩人によって救われます [ref_id:1]。


*** activity_content:
[
  {
    "id": 0,
    "type": "modelQueryPlanning",
    "elapsed_ms": 1396,
    "input_tokens": 1461,
    "output_tokens": 78
  },
  {
    "id": 1,
    "type": "searchIndex",
    "elapsed_ms": 692,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:43:19.760Z",
    "count": 5,
    "search_index_arguments": {
      "search": "おばあさんが出てくるお話",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 2,
    "type": "searchIndex",
    "elapsed_ms": 586,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:43:20.355Z",
    "count": 5,
    "search_index_arguments": {
      "search": "おばあさんが登場する物語",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 3,
    "type": "searchIndex",
    "elapsed_ms": 586,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:43:20.942Z",
    "count": 3,
    "search_index_arguments": {
      "search": "おばあさんが主役の話",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 4,
    "type": "agenticReasoning",
    "reasoning_tokens": 5931,
    "retrieval_reasoning_effort": {
      "kind": "low"
    }
  },
  {
    "id": 5,
    "type": "modelAnswerSynthesis",
    "elapsed_ms": 1176,
    "input_tokens": 3963,
    "output_tokens": 89
  }
]


*** references_content:
[
  {
    "type": "searchIndex",
    "id": "0",
    "activity_source": 1,
    "source_data": {
      "id": "doc8",
      "page_chunk": "マッチ売りの少女 \n寒い大晦日の夜、裸足の少女がマッチを売り歩いていました。誰も買ってく\nれず、帰る家もありません。凍えながらマッチを一本擦ると、暖かいストーブや\nごちそう、優しいおばあさんの幻が見えました。少女は次々とマッチを擦り、\n幸せな光景に包まれます。やがて朝になると、少女は静かに雪の中で眠って\nいました。人々は気づきませんでしたが、少女の心は温かい夢に満ちていま\nした。この物語は、弱い立場の人への思いやりを私たちに問いかけます。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.6337907,
    "doc_key": "doc8"
  },
  {
    "type": "searchIndex",
    "id": "1",
    "activity_source": 1,
    "source_data": {
      "id": "doc7",
      "page_chunk": "赤ずきん \n赤いずきんをかぶった女の子は、おばあさんの家へお見舞いに行く途中でし\nた。森の中で出会ったおおかみは、やさしいふりをして道を聞き出します。おお\nかみは先回りしておばあさんを食べ、赤ずきんを待ち構えました。違和感を\n覚えつつも近づいた赤ずきんは、ついにおおかみに食べられてしまいます。しか\nし、通りかかった狩人が気づき、おおかみのお腹から二人を助け出しました。\n赤ずきんは人を簡単に信じないことの大切さを学び、無事に家へ帰りまし\nた。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.6075602,
    "doc_key": "doc7"
  },
  {
    "type": "searchIndex",
    "id": "2",
    "activity_source": 1,
    "source_data": {
      "id": "doc1",
      "page_chunk": "桃太郎 \nむかしむかし、川上から大きな桃がどんぶらこと流れてきました。洗濯をしてい\nたおばあさんは、その桃を家に持ち帰り、おじいさんと分けようとしました。とこ\nろが桃を割ると、中から元気な男の子が飛び出してきました。二人は大喜\nびでその子を桃太郎と名づけ、大切に育てました。やがて桃太郎は、村を荒\nらす⿁を退治するため旅に出ます。道中で犬、猿、きじと出会い、きびだん\nごを分け与えて仲間にしました。力を合わせて⿁ヶ島に乗り込み、見事⿁を\n退治した桃太郎は、宝物を持って村へ帰り、みんなを幸せにしました。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.5458825,
    "doc_key": "doc1"
  },
  {
    "type": "searchIndex",
    "id": "3",
    "activity_source": 1,
    "source_data": {
      "id": "doc10",
      "page_chunk": "親指姫 \n花の中から生まれた親指ほどの小さな女の子は、親指姫と名づけられまし\nた。ある夜、がまがえるにさらわれ、望まぬ結婚を迫られますが、親切な魚や\nつばめに助けられます。⾧い旅の末、花の国にたどり着いた親指姫は、自分\nと同じ大きさの王子と出会いました。二人は心を通わせ、幸せに暮らしま\nす。親指姫は、自分の居場所を探し続けた末に、本当に安心できる世界\nを見つけたのです。 \n ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.0127609,
    "doc_key": "doc10"
  },
  {
    "type": "searchIndex",
    "id": "4",
    "activity_source": 1,
    "source_data": {
      "id": "doc2",
      "page_chunk": "浦島太郎 \nむかし、浦島太郎という心やさしい若者がいました。ある日、子どもたちにい\nじめられている亀を助けてあげました。すると数日後、その亀が現れ、海の底\nの竜宮城へ案内してくれました。そこでは美しい乙姫が出迎え、浦島太郎\nは夢のような日々を過ごします。しかし村のことが気になり、帰ることにしまし\nた。別れ際、乙姫から玉手箱を渡され、「決して開けてはいけません」と言わ\nれます。地上に戻ると、村の様子はすっかり変わり、知っている人は誰もいま\nせんでした。驚いた浦島太郎が玉手箱を開けると、白い煙が立ちのぼり、た\nちまち老人になってしまいました。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.0019495,
    "doc_key": "doc2"
  }
]

> おばあさんが登場するお話を3つ教えてください
Retrieved content from 'stories-index-knowledge-base' successfully.

*** response_content:
おばあさんが登場するお話は以下の3つです。1つ目は「赤ずきん」で、赤ずきんはおばあさんの家へ向かう途中でおおかみに出会い、最終的におおかみに食べられてしまいますが、狩人によって助けられます [ref_id:0]。2つ目は「桃太郎」で、桃太郎の物語にはおばあさんが登場し、桃を見つけて家に持ち帰るシーンがあります [ref_id:1]。3つ目は「マッチ売りの少女」で、少女が寒い夜におばあさんの幻を見て温かい夢に包まれる場面があります [ref_id:2]。


*** activity_content:
[
  {
    "id": 0,
    "type": "modelQueryPlanning",
    "elapsed_ms": 1442,
    "input_tokens": 1461,
    "output_tokens": 84
  },
  {
    "id": 1,
    "type": "searchIndex",
    "elapsed_ms": 621,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:43:49.374Z",
    "count": 4,
    "search_index_arguments": {
      "search": "おばあさんが登場するお話",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 2,
    "type": "searchIndex",
    "elapsed_ms": 659,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:43:50.034Z",
    "count": 4,
    "search_index_arguments": {
      "search": "おばあさんが主役の物語",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 3,
    "type": "searchIndex",
    "elapsed_ms": 564,
    "knowledge_source_name": "stories-index-knowledge-source",
    "query_time": "2026-02-02T07:43:50.599Z",
    "count": 6,
    "search_index_arguments": {
      "search": "おばあさんが出てくる童話",
      "source_data_fields": [
        {
          "name": "page_chunk"
        },
        {
          "name": "id"
        },
        {
          "name": "story_title"
        },
        {
          "name": "source_file"
        }
      ],
      "search_fields": [],
      "semantic_configuration_name": "stories-index-semantic-config"
    }
  },
  {
    "id": 4,
    "type": "agenticReasoning",
    "reasoning_tokens": 5931,
    "retrieval_reasoning_effort": {
      "kind": "low"
    }
  },
  {
    "id": 5,
    "type": "modelAnswerSynthesis",
    "elapsed_ms": 2063,
    "input_tokens": 4185,
    "output_tokens": 191
  }
]


*** references_content:
[
  {
    "type": "searchIndex",
    "id": "0",
    "activity_source": 3,
    "source_data": {
      "id": "doc7",
      "page_chunk": "赤ずきん \n赤いずきんをかぶった女の子は、おばあさんの家へお見舞いに行く途中でし\nた。森の中で出会ったおおかみは、やさしいふりをして道を聞き出します。おお\nかみは先回りしておばあさんを食べ、赤ずきんを待ち構えました。違和感を\n覚えつつも近づいた赤ずきんは、ついにおおかみに食べられてしまいます。しか\nし、通りかかった狩人が気づき、おおかみのお腹から二人を助け出しました。\n赤ずきんは人を簡単に信じないことの大切さを学び、無事に家へ帰りまし\nた。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.7408404,
    "doc_key": "doc7"
  },
  {
    "type": "searchIndex",
    "id": "1",
    "activity_source": 3,
    "source_data": {
      "id": "doc1",
      "page_chunk": "桃太郎 \nむかしむかし、川上から大きな桃がどんぶらこと流れてきました。洗濯をしてい\nたおばあさんは、その桃を家に持ち帰り、おじいさんと分けようとしました。とこ\nろが桃を割ると、中から元気な男の子が飛び出してきました。二人は大喜\nびでその子を桃太郎と名づけ、大切に育てました。やがて桃太郎は、村を荒\nらす⿁を退治するため旅に出ます。道中で犬、猿、きじと出会い、きびだん\nごを分け与えて仲間にしました。力を合わせて⿁ヶ島に乗り込み、見事⿁を\n退治した桃太郎は、宝物を持って村へ帰り、みんなを幸せにしました。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.700431,
    "doc_key": "doc1"
  },
  {
    "type": "searchIndex",
    "id": "2",
    "activity_source": 3,
    "source_data": {
      "id": "doc8",
      "page_chunk": "マッチ売りの少女 \n寒い大晦日の夜、裸足の少女がマッチを売り歩いていました。誰も買ってく\nれず、帰る家もありません。凍えながらマッチを一本擦ると、暖かいストーブや\nごちそう、優しいおばあさんの幻が見えました。少女は次々とマッチを擦り、\n幸せな光景に包まれます。やがて朝になると、少女は静かに雪の中で眠って\nいました。人々は気づきませんでしたが、少女の心は温かい夢に満ちていま\nした。この物語は、弱い立場の人への思いやりを私たちに問いかけます。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.6961775,
    "doc_key": "doc8"
  },
  {
    "type": "searchIndex",
    "id": "3",
    "activity_source": 3,
    "source_data": {
      "id": "doc2",
      "page_chunk": "浦島太郎 \nむかし、浦島太郎という心やさしい若者がいました。ある日、子どもたちにい\nじめられている亀を助けてあげました。すると数日後、その亀が現れ、海の底\nの竜宮城へ案内してくれました。そこでは美しい乙姫が出迎え、浦島太郎\nは夢のような日々を過ごします。しかし村のことが気になり、帰ることにしまし\nた。別れ際、乙姫から玉手箱を渡され、「決して開けてはいけません」と言わ\nれます。地上に戻ると、村の様子はすっかり変わり、知っている人は誰もいま\nせんでした。驚いた浦島太郎が玉手箱を開けると、白い煙が立ちのぼり、た\nちまち老人になってしまいました。 ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.058133,
    "doc_key": "doc2"
  },
  {
    "type": "searchIndex",
    "id": "4",
    "activity_source": 3,
    "source_data": {
      "id": "doc10",
      "page_chunk": "親指姫 \n花の中から生まれた親指ほどの小さな女の子は、親指姫と名づけられまし\nた。ある夜、がまがえるにさらわれ、望まぬ結婚を迫られますが、親切な魚や\nつばめに助けられます。⾧い旅の末、花の国にたどり着いた親指姫は、自分\nと同じ大きさの王子と出会いました。二人は心を通わせ、幸せに暮らしま\nす。親指姫は、自分の居場所を探し続けた末に、本当に安心できる世界\nを見つけたのです。 \n ",
      "story_title": "桃太郎",
      "source_file": "stories.pdf"
    },
    "reranker_score": 2.0516639,
    "doc_key": "doc10"
  }
]

>
終了します。
(.venv) PS C:\>
```