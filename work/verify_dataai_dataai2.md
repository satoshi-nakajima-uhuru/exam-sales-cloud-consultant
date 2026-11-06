# dataai.json / dataai2.json 検証結果

確認した問題: 59問（DA-001〜DA-034、DA2-001〜DA2-025）

| 問題ID | 種別 | 理由 | 根拠URL |
|---|---|---|---|
| DA-026 | 答え変更・選択肢修正・解説修正 | Summer '25 の「Salesforce 活動としてメールを同期」で取り込みメールは Task/EmailMessage として保存され標準レポート対象になる。旧正解（標準レポートは制限される）は現行仕様と矛盾。Activity 360 レポート/活動指標は廃止予定。選択肢を全面改訂し正解を新選択肢0に | https://help.salesforce.com/s/articleView?id=sales.eac_email_activity.htm&language=en_US&type=5 / https://help.salesforce.com/s/articleView?id=004633781&language=en_US&type=1 |
| DA-016 | 選択肢修正・解説修正 | 積み上げ集計項目の絞り込み条件では「今年度」等の相対日付が使えないため、「今年度」条件を問題文と正解選択肢から除去 | https://help.salesforce.com/s/articleView?id=sf.fields_about_roll_up_summary_fields.htm&language=en_US&type=5 |
| DA-029 | 選択肢修正・解説修正 | SDR エージェントは Lead Nurturing を経て Agentforce Engagement に名称変更（2026年8月）。名称に依存しない記述に変更。打ち合わせ設定の要件を「営業担当者につなぐ」に修正 | https://help.salesforce.com/s/articleView?language=en_US&id=release-notes.rn_sales_agents_ln_engagement_name_update.htm&release=264&type=5 / https://help.salesforce.com/s/articleView?id=sales.sales_agent_sdr_parent.htm&language=en_US&type=5 |
| DA-033 | 選択肢修正・解説修正 | ZDR は顧客が LLM 提供元と契約するのではなく Salesforce と提供元間の取り決め。データマスキングは Agentforce エージェントでは無効である旨を補足 | https://trailhead.salesforce.com/content/learn/modules/llm-data-masking-in-the-einstein-trust-layer/explore-llm-data-masking |
| DA2-023 | 解説修正 | データマスキングは Agentforce エージェントでは無効である旨を補足 | 同上 |
| DA-027 | 解説修正 | 2026年4月以降トピックは「サブエージェント」に名称変更されたことを補足 | https://www.salesforce.com/agentforce/legacy-guide/ |
| DA2-021 | 解説修正 | 同上 | https://www.salesforce.com/agentforce/legacy-guide/ |
| DA2-022 | 解説修正 | 同上 | https://www.salesforce.com/agentforce/legacy-guide/ |
| DA-019 | 解説修正 | Data Cloud は 2025年10月に Data 360 へ名称変更されたことを補足 | https://developer.salesforce.com/docs/data/data-cloud-int/guide |
| DA-008 | 解説修正 | choiceNotes[4] の「ユーザーごとの既定値という標準機能はない」は既定値の数式で $User 参照が可能なため不正確。既定値は空白保存を防げない旨に修正 | https://help.salesforce.com/s/articleView?id=sf.customize_functions_default_values.htm&type=5 |
| DA2-016 | 解説修正 | 「協調的売上予測」を公式日本語名「コラボレーション売上予測」に統一 | https://help.salesforce.com/s/articleView?id=sales.forecasts3_einstein_about.htm&type=5 |

その他の48問は、正解、他の選択肢、解説、choiceNotes に問題はなかった。削除した問題はない。
