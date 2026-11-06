# lifecycle.json / lifecycle2.json 校閲結果

確認: 47問（lifecycle 22 / lifecycle2 25）。答え変更・削除なし。

| 問題ID | 種別 | 理由 | 根拠URL |
|---|---|---|---|
| SL-007 | 解説修正 | choiceNotes[3]: 標準のメール項目は一意属性を設定できない点を追記し、「リード同士の一意性は担保できる」と読める記述を訂正 | https://help.salesforce.com/s/articleView?id=sf.duplicate_rules_map_of_reference.htm |
| SL-008 | 解説修正 | 最初の接点・最後の接点・均等配分は Account Engagement 利用時の追加モデル。標準では主キャンペーンソースモデル＋カスタムモデルである旨に訂正 | https://help.salesforce.com/s/articleView?language=en_US&id=sales.campaigns_influence_customizable_understanding.htm |
| SL-018 | 解説修正 | choiceNotes[1]: 「売上予測階層は組織に1つ」を、ロール階層／テリトリー階層に基づく構造という表現に訂正 | https://help.salesforce.com/s/articleView?id=sf.forecasts3_hierarchy.htm |
| SL-021 | 解説修正 | 設定画面（Forecast Quotas）でもノルマを手入力できるようになったため、「APIツールが唯一」と読める解説を、大量・定期登録にはAPIツールが適するという表現に修正 | https://help.salesforce.com/s/articleView?language=en_US&id=sales.forecasts3_quotes_intro.htm |
| SL2-009 | 選択肢修正 | 選択肢4「計画状態のモデルは常に1つだけ」はエディションごとのモデル数上限に依存するため、「計画状態では割り当てルールを実行できない」（明確に誤り）に差し替え | https://help.salesforce.com/s/articleView?id=sales.tm2_preview_account_assignments.htm&language=en_US&type=5 |
| SL2-018 | 解説修正 | choiceNotes[2]: 割り当てルールに一致しないリードはリード設定の「デフォルトのリード所有者」に割り当てられる。デフォルトのリード作成者が所有者になるのは有効な割り当てルールがない場合なので訂正 | https://help.salesforce.com/s/articleView?id=sf.setting_up_web-to-lead.htm |
| SL2-021 | 解説修正 | choiceNotes[0]: 「無効な価格表にも追加できる」は公式に確認できないため、その細部に依存しない理由に書き換え | https://help.salesforce.com/s/articleView?id=sf.products_pricebooks.htm |

## 主な確認済み事項（変更なし）
- SL2-003: マネージャー調整を無効化すると既存の調整は削除される — https://help.salesforce.com/s/articleView?id=sf.forecasts3_disabling_help.htm&language=en_US&type=5
- SL2-004: 売上予測通貨は会社の通貨／個人通貨を選択できる — https://help.salesforce.com/s/articleView?id=forecasts3_enabling_forecasts_currency.htm&language=en_US
- SL2-024: 注文の取引先と契約の取引先は一致が必要 — https://help.salesforce.com/s/articleView?id=order_edit.htm&language=en_US&type=5
