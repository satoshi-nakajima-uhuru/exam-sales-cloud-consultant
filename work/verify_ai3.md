# ai3.json 検証結果

確認: 30問 / 修正: 4問（選択肢修正1、解説修正3）/ 削除: なし

| 問題ID | 種別 | 理由 | 根拠URL |
|---|---|---|---|
| AI3-007 | 選択肢修正（問題文・解説も修正） | Summer '25 以降、活動キャプチャのメールを ToDo/EmailMessage として同期する「Sync Email as Salesforce Activity」が提供され、有効にすれば既存の活動レポートで集計できる。「標準の構成では保存されない」が一律には成り立たなくなったため、従来のストレージ構成であることを問題文に明記し、正解の選択肢に移行の選択肢を追加した | https://help.salesforce.com/s/articleView?language=en_US&id=sales.eac_email_activity.htm&type=5 / https://help.salesforce.com/s/articleView?id=release-notes.rn_sales_productivity_eac_email_sync.htm&language=en_US&release=256&type=5 |
| AI3-023 | 解説修正 | Agentforce のエージェントではLLM向けのデータマスキングが無効化されている点を追記した（Prompt Builder など、エージェント以外の機能では引き続き有効） | https://trailhead.salesforce.com/content/learn/modules/llm-data-masking-in-the-einstein-trust-layer/explore-llm-data-masking / https://www.salesforce.com/blog/llm-data-masking/ |
| AI3-026 | 解説修正 | Data Cloud が2025年10月に Data 360 へ名称変更されたことを追記した | https://help.salesforce.com/s/articleView?language=en_US&id=data.c360_a_data_cloud.htm&type=5 |
| AI3-027 | 解説修正 | 同上 | https://www.salesforce.com/data/ |

## 未修正の懸念点
- AI3-008: 「Sync Email as Salesforce Activity」を有効にした構成では、同期されたメールの公開範囲が活動キャプチャの共有設定ではなく ToDo の共有モデルに従う可能性がある。公式情報では確認できていない。
- AI3-010/016/017: Agentforce アシスタントと Agent Builder は名称が変わっている（Agentforce の既定の社員向けエージェント、Agentforce Builder）。問題が名称そのものを問うものではないため、そのまま残した。
