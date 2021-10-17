
# # import requests

# # # req_json = 
# # req_json = {"name":"ankit",
# #             "age": 28}

# # # url = f"http://127.0.0.1:8000/{req_json}"

# # data = requests.post(url)

# # print(data.text)

# # decorator



# def outer_func(hello_func):
#     def inner_func(*args,**kwargs):
#         try:
#             hello_func(*args,**kwargs)

#         except Exception as e:
#             print(e)
#     return inner_func

# message = 1234
# count = 0
# # @outer_func
# def hello_func(message):
#     global count
#     if type(message) == str:
#         count += 0
#         if count >1:
#             print(count)
#             return
#         hello_func(message)
#         print(f"i am executing {message}")
#         # message = None
#     else:
#         hello_func(message = None)

# if __name__ == "__main__":
#     hello_func(message)
# warranty_contract_property_hudi = spark.read.format("org.apache.hudi").load('s3://analytics-edl-stage-dev/warranty-harmony/warranty_contract/warranty_contract_property_tbl/*')
# from pyspark.sql import SparkSession
# import pyspark.sql.functions as sqlfunc
# from pyspark.sql.types import *
# import argparse, sys
# from pyspark.sql import *
# import pyspark.sql.functions as sqlfunc
import pandas as pd
pandas_warranty_contract_property_hudi = warranty_contract_property_hudi.to_pandas()
df = pandas_warranty_contract_property_hudi
import pandas as pd
# df = reading from property table
pandas_consolidated_df_final = consolidated_df_final.to_pandas()
df2 = pandas_consolidated_df_final
number_of_rows = df2.shape[0]
tradein_property_list = ['TradeIn_Amount','TradeIn_brandName','TradeIn_merchLineSeqNum','TradeIn_merchQuantitySeqNum','TradeIn_merchRegisterNum','TradeIn_merchReplacedDate','TradeIn_merchStoreNum','TradeIn_merchTransactionNum']
replaced_property_list = ['REPLACED_Amount','REPLACED_brandName','REPLACED_merchLineSeqNum','REPLACED_merchQuantitySeqNum','REPLACED_merchRegisterNum','REPLACED_merchReplacedDate','REPLACED_merchStoreNum',"REPLACED_merchTransactionNum"]
def ret_col(prp): #df2 : df => 1:8; df2 -> Dest Col | df -> Source Col
    p1 = []
    for cid in df2['warranty_contract_id']:
        ar = df['property_value'].loc[(df['property_name'] == prp ) & (df['warranty_contract_id'] == cid)].tolist()
        p1.append(ar[0])
        return p1
# for i in range(len(df['property_name'],0,8):
#     if df['property_name'][i].startswith('replaced_'):
for property in replaced_property_list:
    df2[property] = ret_col(property)
    # if df['property_name'][i].startswith('tradein_'):
for property in tradein_property_list:
    df2[property] = ret_col(property)

df_sp = spark_session.createDataFrame(df_pd)


