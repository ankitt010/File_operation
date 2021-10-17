# # # decorator

# # import functools
# # from time import perf_counter

# # import decorator

# # def decorator_func_argument(a1,a2,a3):
# #     def func_decorator(func):
# #         print(a1,a2,a3)
# #         @functools.wraps(func)
# #         def inner_func(*args,**kwargs):
# #             print('hello guys i am back')
# #             try:
# #                 func(*args,**kwargs)
# #             except Exception as e:
# #                 print(e)
# #             return 
# #         return inner_func
# #     return func_decorator

# # @decorator_func_argument('hello','world',42)
# # def func(number):
# #     # sum = 0
# #     sum = number + number
# #     return number

# # if __name__ == '__main__':
# #     func(100)
# import pandas as pd
# import numpy as np
# from pandas._libs.tslibs.timestamps import Timestamp


# changed_dict = {
#     'warranty_contract_id': np.int64 ,
# 'external_contract_id': object ,
# 'vendor_contract_id': object ,
# 'warranty_plan_code': object ,
# 'price_tier_id': np.int64,
# 'crmcustomer_id': object ,
# 'purchaser_first_name': object ,
# 'purchaser_last_name': object ,
# 'warrantee_first_name': object, 
# 'warrantee_last_name': object ,
# 'warrantee_email': object, 
# 'warr_transaction_num': object ,
# 'warr_transaction_date':'datetime64[ns]', 
# 'warr_store_num': object ,
# 'warr_sku': object ,
# 'warr_register_num': np.int64 ,
# 'warr_line_seq_num': np.int64 ,
# 'warr_price': np.float64, 
# 'warr_tax': np.float64 ,
# 'merch_transaction_num': object ,
# 'merch_sold_date': 'datetime64[ns]' , #needs to be changed
# 'merch_store_num': object ,
# 'merch_register_num': np.int64 ,
# 'merch_line_seq_num': np.int64 ,
# 'merch_sku': object ,
# 'return_transaction_num': object,
# 'return_date': 'datetime64[ns]' ,#changed needed
# 'return_store_num': object ,
# 'return_line_seq_num': np.int64, 
# 'return_amount': np.float64, 
# 'limit_of_liability': np.float64, 
# 'total_deductible': np.float64, 
# 'valid_from':'datetime64[ns]',  
# 'valid_to': 'datetime64[ns]', 
# 'created_by': object ,
# 'created_date': 'datetime64[ns]',#needs to be changed 
# 'updated_by': object ,
# 'updated_date': 'datetime64[ns]', #timestamp
# 'brand_name': object ,
# 'jcid': np.int64, 
# 'merch_tax': np.float64, 
# 'return_register_num': object, 
# 'vendor_comments': object ,
# 'warrantee_address_line1': object ,
# 'warrantee_address_line2': object ,
# 'warrantee_city': object ,
# 'warrantee_country': object ,
# 'warrantee_phone': np.int64 ,
# 'warrantee_state': object ,
# 'warrantee_zip': object ,
# 'warranty_document_url': object ,
# 'merch_quantity_sequence': np.int64, 
# 'verbiage_id': np.int64, 
# 'merch_retail_price' :np.float64 
# }

# df = pd.DataFrame(columns=changed_dict)
# print(df)
# # warr_contract_status_df
# changed_dict = {
#     'warranty_contract_id': np.int64,
# 'crmcustomer_id': object, 
# 'created_date': 'datetime64[ns]' ,
# 'status_id' :np.int64, 
# 'warranty_contract_status_id':  np.int64
# }
# # contract_property
# changed_dict = {'warranty_contract_property_id': np.int64,
# 'warranty_contract_id':  np.int64,
# 'property_name':object,  'property_value' :object ,
# 'is_deleted': object 
# }
# # print(pd.Timestamp)
print(b"abcde".decode("utf-8") )
