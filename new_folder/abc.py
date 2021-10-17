prop = [
        StructField("warranty_contract_id", IntegerType(),True),
        StructField("external_contract_id", StringType(),True),
        StructField("warranty_plan_id", FloatType(),True),
        StructField("warranty_plan_code", StringType(),True),
        StructField("price_tier_id", IntegerType(),True),
        StructField("purchaser_first_name", StringType(),True),
        StructField("purchaser_last_name", StringType(),True),
        StructField("warrantee_email", StringType(),True),
        StructField("warrantee_first_name", StringType(),True),
        StructField("warrantee_last_name", StringType(),True),
        StructField("warr_transaction_date", DateType(),True),
        StructField("warr_register_num", IntegerType(),True),
        StructField("warr_line_seq_num", IntegerType()),
        StructField("warr_price", FloatType(),True),
        StructField("warr_tax", FloatType(),True),
        StructField("merch_transaction_num", StringType(),True),
        StructField("merch_register_num", IntegerType(),True),
        StructField("merch_retail_price", FloatType(),True),
        StructField("merch_sold_date", DateType(),True),
        StructField("merch_line_seq_num", IntegerType(),True),
        StructField("return_amount", FloatType(),True),
        StructField("return_date", DateType(),True),
        StructField("return_register_num", StringType(),True),
        StructField("return_line_seq_num", IntegerType(),True),
        StructField("brand_name",StringType(),True),
        StructField("jcid", IntegerType(),True),
        StructField("merch_tax", FloatType(),True),
        StructField("vendor_comments", StringType(),True),
        StructField("warrantee_address_line1", StringType(),True),
        StructField("warrantee_address_line2", StringType(),True),
        StructField("warrantee_city", StringType(),True),
        StructField("warrantee_country", StringType(),True),
        StructField("warrantee_phone",LongType(),True),
        StructField("warrantee_state", StringType(),True),
        StructField("warrantee_zip", StringType(),True),
        StructField("merch_store_num", StringType(),True),
        StructField("return_store_num", FloatType(),True),
        StructField("customer_id", FloatType(),True),
        StructField("warr_transaction_num", StringType(),True),
        StructField("return_transaction_num", FloatType(),True),
        StructField("warr_store_num", StringType(),True),
        StructField("warranty_sku", FloatType(),True),
        StructField("merch_sku", FloatType(),True),
        StructField("warranty_document_url", StringType(),True),
        StructField("merch_quantity_sequence", StringType(),True),
        StructField("source", StringType(),True),
        StructField("status_id", IntegerType(),True),
        StructField("status_description", StringType(),True),
        StructField("return_date_timestamp", TimestampType(),True),
        StructField("last_modified_date", DateType(),True),
        StructField("run_date", DateType(),True),
        StructField("run_time", TimestampType(),True),
        StructField("REPLACED_Amount", FloatType(),True),
        StructField("REPLACED_brandName", StringType(),True),
        StructField("REPLACED_merchLineSeqNum", IntegerType(),True),
        StructField("REPLACED_merchQuantitySeqNum", IntegerType(),True),
        StructField("REPLACED_merchRegisterNum", IntegerType(),True),
        StructField("REPLACED_merchREPLACEDDate", DateType(),True),
        StructField("REPLACED_merchStoreNum", StringType(),True),
        StructField("REPLACED_merchTransactionNum", StringType(),True),
        StructField("TradeIn_Amount", FloatType(),True),
        StructField("TradeIn_brandName", StringType(),True),
        StructField("TradeIn_merchLineSeqNum", IntegerType(),True),
        StructField("TradeIn_merchQuantitySeqNum", IntegerType(),True),
        StructField("TradeIn_merchRegisterNum", IntegerType(),True),
        StructField("TradeIn_merchREPLACEDDate", DateType(),True),
        StructField("TradeIn_merchStoreNum", StringType(),True),
        StructField("TradeIn_merchTransactionNum", StringType(),True),
    ]