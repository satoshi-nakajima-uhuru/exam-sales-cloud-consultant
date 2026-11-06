# lifecycle3.json / data3.json 校閲結果

確認問題数: 50（SL3-001〜025、DM3-001〜025）。答え変更・削除なし。

| 問題ID | 種別 | 理由 | 根拠URL |
|---|---|---|---|
| SL3-001 | 選択肢修正・解説修正 | 選択肢0「リードの販売プロセス」は存在しない機能名で、注記の「販売プロセスはリードに関係しない」はリードプロセス（リードのレコードタイプ用）の存在と紛らわしかった。そこで選択肢を「商談の販売プロセス」に変え、解説にリードプロセスの補足を追加した。 | https://help.salesforce.com/s/articleView?id=sales.leads_convert_settings.htm&type=5 |
| SL3-013 | 解説修正（choiceNotes[1]） | 「承認プロセスのアクションでは商談を作成できない」という断定は、現行の承認アクションの仕様（フロー連携など）次第で揺らぐ。そこで要件との不一致を理由とする記述に変えた。 | https://help.salesforce.com/s/articleView?id=platform.approvals_creating_approval_processes.htm&type=5 |
| SL3-015 | 解説修正 | 「有効にできるアラートは1つ」「会社の通貨で評価」は公式ヘルプで確認できなかったため（ページがJS描画で取得できず）、この細部に依存しない記述にした。 | https://help.salesforce.com/s/articleView?id=sales.customize_oppalerts.htm&type=5 |
| DM3-003 | 解説修正 | 外部オブジェクトを標準オブジェクト（取引先）の子として関連付けるのは「間接参照関係」。「外部参照関係」は親が外部オブジェクトのときに使う関係のため訂正した。 | https://help.salesforce.com/s/articleView?id=platform.external_object_relationships.htm&type=5 |
| DM3-009 | 解説修正 | 付与する権限を「後者のみ」とした記述を「両権限を付与」に変えた。データ移行の一般的な手順に合わせたもの。 | https://help.salesforce.com/s/articleView?id=000334139&type=1 |
| DM3-013 | 解説修正 | Data Cloud が2025年10月に Data 360 へ名称変更されたことを補足した。 | https://www.salesforce.com/news/ （Dreamforce 2025 発表）/ https://www.salesforceben.com/salesforce-data-cloud-renamed-to-data-360-as-part-of-agentforce-360/ |

## 残した懸念点
- SL3-002: 設定の日本語ラベル「取引開始済みリードの入力規則を必須にする」（英語 "Require Validation for Converted Leads"）は、実際のUI表記と一字一句同じかは確認できていない。
- DM3-011: 製品名は現行の "Salesforce Backup & Recover" で確認できた。名称が変わりやすいので注意が必要。
- DM3-013/014/015: 「Data Cloud」表記は残した（試験範囲の表記に合わせたもの）。
- SL3-011: Classic の標準「競合相手」関連リストには触れていない。拡張性・分析の観点では、正解（連結オブジェクト）は妥当と判断した。
