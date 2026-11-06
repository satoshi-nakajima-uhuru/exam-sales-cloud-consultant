# consulting2.json 検証結果

確認: 25問 / 修正: 3問（選択肢修正2、解説修正2、重複あり） / 削除: なし

| 問題ID | 種別 | 理由 | 根拠URL |
|---|---|---|---|
| CI2-008 | 選択肢修正・解説修正 | 正解の選択肢が「権限セットグループをコピー」という公式に確認できない操作に依存していたため、「同じ権限セットを含む別のグループを作る」に変更。ミュート権限セットは1グループに1つだけで、プロファイルなど別経路の付与は打ち消せないことを解説に追記。 | https://help.salesforce.com/s/articleView?id=platform.perm_set_groups_muting.htm&language=en_US&type=5 |
| CI2-018 | 選択肢修正 | 正解の選択肢が「レコード更新時の高速項目更新」となっていたが、要件は作成・更新の両方。Flow Builder の設定（起動条件「作成または更新」、最適化「高速項目更新」）に合わせた表現に修正。 | https://help.salesforce.com/s/articleView?id=platform.flow_concepts_trigger_record.htm&type=5 |
| CI2-022 | 解説修正 | 外部オブジェクトを取引先（標準オブジェクト）の関連リストに出すには間接参照関係を使う。外部参照関係は親が外部オブジェクトの場合なので、解説の「外部参照関係など」は誤り。 | https://help.salesforce.com/s/articleView?id=sf.external_object_relationships.htm&language=en_US&type=5 |
