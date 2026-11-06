# practical.json / practical2.json 校閲結果

確認: 51問（practical 26 / practical2 25）。答え変更 0、削除 0。

| 問題ID | 種別 | 理由 | 根拠URL |
|---|---|---|---|
| PA-003 | 解説修正 | choiceNotes[0]「標準ナビゲーションではリストとレコードを同時に表示できない」は誤り（Summer '20 から標準ナビゲーションでも分割ビューを利用可能）。タブ追加では解決しない、という理由に変更 | https://www.salesforce.com/blog/summer-20-release-treasure-features/ |
| PA-006 | 選択肢修正 | 正解の選択肢1「キャプチャメールは標準活動レコードとして保存されずレポート不可」は Summer '25 の Sync Email as Salesforce Activity（Task/EmailMessage として保存しレポート可）により現行仕様と合わない。選択肢0/1を除外設定（正解）と手動記録必須（誤り）に差し替え、解説を修正 | https://help.salesforce.com/s/articleView?id=sales.eac_email_activity.htm&type=5 , https://help.salesforce.com/s/articleView?id=sales.eac_email_activity_considerations.htm&type=5 |
| PA-007 | 解説修正 | choiceNotes[0]の「活動キャプチャのメールは標準レコードにならず」を削除し、自動取り込みのため選択的記録の要件に合わない、という理由に変更 | 同上 |
| PA-018 | 解説修正 | ワークフロールール／プロセスビルダーは「廃止予定」ではなく2025年12月31日にサポート終了済み | https://admin.salesforce.com/ （End of Support for Workflow Rules and Process Builder 告知）, https://www.salesforceben.com/salesforce-announces-end-of-support-for-workflow-rules-process-builder/ |
| PA2-001 | 解説修正 | choiceNotes[3]「積み上げ集計に期間条件を付けても実現は可能」は不正確（積み上げ集計の条件に相対日付は使いにくい）ため修正 | 公式確認できず（表現を弱めて対応） |
| PA2-002 | 選択肢修正 | 保存済みレポートタイプの関係変更可否が公式で確認できないため、「with or without の関係を設定したカスタムレポートタイプでレポートを作成する」に書き換え | https://help.salesforce.com/s/articleView?id=analytics.reports_defining_report_types.htm&type=5 |
| PA2-017 | 選択肢修正 | メールアプリケーションペインの割り当ては Lightning アプリケーションビルダーの有効化で組織デフォルト／プロファイル単位。「Outlook インテグレーション設定でユーザーに割り当て」は不正確 | https://developer.salesforce.com/docs/platform/lwc/guide/use-config-for-app-builder-email-app-pane.html |

## 残した懸念点
- PA2-005: Lightning レポートの条件付き書式が表形式で使えない点は公式ヘルプを直接確認できず（二次情報では集計/マトリックスのみで一致）。
- PA2-007: 動的ダッシュボード上限（EE 5 / UE・PE 10）は二次情報で一致、公式ヘルプ未取得。
- PA-017/PA2-018〜020: 従来の承認プロセスを前提。2026年時点でフロー承認（Approval Orchestration）も推奨されつつあるが、承認プロセス自体は利用可能なため据え置き。
