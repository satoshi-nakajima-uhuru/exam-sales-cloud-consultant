# practical3.json 校閲結果

確認: 30問 / 修正: 3問（選択肢修正2、解説修正1）/ 削除: 1問（PA3-017）

| 問題ID | 種別 | 理由 | 根拠URL |
|---|---|---|---|
| PA3-005 | 解説修正（choiceNotes[1]） | 「かんばんで分けられるのは選択リスト項目」はリードソース（選択リスト）でも列分けできるため誤解を招く。グラフにならない点を理由に書き換え | 既知の仕様（かんばんは選択リスト項目でグループ化）。URL未確認 |
| PA3-007 | 選択肢修正（choices[0]・解説・choiceNotes[0][2]） | 取引先の一括譲渡では、元の所有者が所有する進行中の商談は自動で譲渡され、オプションは「取引先所有者以外が所有する進行中の商談」「完了した商談」の譲渡。「進行中の商談も譲渡する選択肢を付けて」は不正確。choiceNotes[2] は確認できない挙動（インポート時の関連商談）への依存を除去 | https://developer.salesforce.com/docs/atlas.en-us.246.0.api.meta/api/sforce_api_header_ownerchangeoptions.htm （ヘルプ本文 sf.admin_transfer.htm は取得不可） |
| PA3-017 | 削除 | 正解の根拠である「ニュース」コンポーネントと Einstein アカウントインサイトは Winter '24（2023年）で廃止済み。2026年時点の現行機能で正解を一意に確定できないため削除 | Winter '24 リリースノート（Sales Cloud の廃止機能）。公式ページは取得できず、二次情報（2023年10月13日廃止）で確認。 |
| PA3-029 | 選択肢修正（choices[0]・解説） | Trailhead のモジュール見出しが「Agentforce Sales Everywhere」になっており製品名が変遷中のため、「Salesforce が提供する Chrome 拡張機能（Sales Cloud Everywhere）」として名称に依存しない表現に。答えは変更なし | https://trailhead.salesforce.com/content/learn/modules/sales-cloud-everywhere-for-sales-teams/learn-about-sales-cloud-everywhere |

## 確認済みで修正不要とした主な事実
- PA3-003: ホームページの割り当ては組織デフォルト／アプリデフォルト／アプリとプロファイルの3段階
- PA3-008/009: グローバルの作成アクションは表示中のレコードと関連付かない。レコード更新アクションはオブジェクト固有のみで、定義済み項目値を設定できる
- PA3-012: 制御項目は選択リスト（標準可）とチェックボックス。複数選択リストは従属項目のみ
- PA3-021: カレンダーの組織の共有設定（詳細を非表示〜フルアクセス）
- PA3-025: レポートフォルダの閲覧者／編集者／管理者の権限差
