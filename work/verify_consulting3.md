# consulting3.json 校閲結果

確認: 30問 / 修正: 2問（選択肢修正1、解説修正1）/ 削除: なし

| 問題ID | 種別 | 理由 | 根拠URL |
|---|---|---|---|
| CI3-013 | 選択肢修正（正解選択肢・解説・choiceNotes・ref） | Salesforce Optimizer アプリは Winter '26（Hyperforce 組織）／Summer '26（それ以外）で廃止済みのため、2026年時点で「最初に Optimizer を実行する」は誤り。正解をメタデータと利用状況の棚卸し（入力率・使用場所・プロファイル/権限セット・レイアウト/自動化の一覧化）に書き換え。答えの位置（0）は変更なし | https://trailhead.salesforce.com/trailblazer-community/feed/0D5KX00000mlut50AA , https://help.salesforce.com/s/articleView?id=Salesforce-Feature-Retirements&language=en_US&type=1 |
| CI3-018 | 解説修正（choiceNotes[3]） | 「Sandbox には独自の資格情報があり本番の情報は使わない」は不正確。Sandbox の作成・更新時に本番のユーザー情報（パスワード含む）がコピーされ、ユーザー名に Sandbox 名が付加される | https://help.salesforce.com/s/articleView?id=sf.data_sandbox_create.htm&type=5 |

## 確認済みで修正不要とした主な事実
- CI3-012: Professional Edition の API はアドオン（Web Services API）購入が必要 — https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api/intro_rest_compatible_editions.htm
- CI3-015: ワークフロールール/プロセスビルダーは 2025年12月31日でサポート終了
- CI3-017: Sandbox 更新間隔 Developer/Developer Pro 1日、Partial 5日、Full 29日
