# token='eyJhbGciOiJSUzI1NiIsImtpZCI6IjVDMkQwMEFBRTEwNDcxM0EyQzI0NjhGNDQ2MEQwQkE4NkRENjMzNTYiLCJ0eXAiOiJhdCtqd3QiLCJ4NXQiOiJYQzBBcXVFRWNUb3NKR2owUmcwTHFHM1dNMVkifQ.eyJuYmYiOjE2MzIxMjgzMDIsImV4cCI6MTYzMjEzOTEwMiwiaXNzIjoiaHR0cHM6Ly9zaWduZXQtaWRlbnRpdHktcHJvdmlkZXItdGVzdC5qZXdlbHMuY29tIiwiYXVkIjoiV2FycmFudHlBUEkiLCJjbGllbnRfaWQiOiJFRFciLCJzY29wZSI6WyJXYXJyYW50eUFQSS5BZG1pbkFjY2VzcyJdfQ.Fffz0NhGq0TjpJBVHXzrtQLX76FSwPbwmjRxQLgpgP0Ic9HUzhldtlCLeMYQx3GFWMqpMtzPpgKXfJCHjQsv0RaLlow8UGLcDdplpqvXeRL65VGj_2fMPsqFEvwVhZk732JVYbkXzjNKSqwILsK0FWd5VnhIj0z-2I8pNQEDIsmd7zTFlBudTWK9QJDE24LbdDji128HQg_ELuk7Tej-QKkru6Epw9JiSvzcGm0KUkGaI3IoGtKihvl-khJAoIF24NA_qu3IOkcgELT59BQGyfUee6fnvXgQlrDF1JdQJBKjwmaIaJjo0m9gQfa6y9CAyMbxqJxmc2cCypq4GjUZxA'
# import requests
# import json
# formats='json'
# headers={
#     "accept":"application/json",
#     "Content-Type":"application/json",
#     "SharedAccessKeyName":"AnalyticsTeam",
#     "Authorization": f"Bearer {token}",
#     "EntityPath":"warranty-contracts",
#     "SharedAccessKey":"cxrzeCDVlqJhFNFB/L8nBGDpybYc9iYIebAYI+bbQjs="
# }
# body={
#     "warrTransactionDateFrom": "2020-12-21T00:00:00Z", 
#       "warrTransactionDateTo": "2020-12-25T23:59:59Z"
 
# }
 
# data_arr = []
# flat_list=[]
# count=0
# for i in range(1,500):
#   url = f'https://sig-warrantysystemofrecord-usc-perf-api.azurewebsites.net/api/v1/WarrantyContracts?pagenumber={i}'
#   jsonObject = json.dumps(body)
#   response = requests.post(url, headers=headers, data=jsonObject)
#   print("Status Code", response.status_code)
#   if(response.status_code == 200):
#     count=count+1
#     data_arr.append(json.loads(response.text))
#   elif(response.status_code == 204):
#     break
# print(count)
# with open(r"WarrantyContract2020-dec-05.json", "w") as write_file:
#       json.dump(data_arr, write_file)
# import json
# import pandas as pd
# json_string = {"ankit":[230,34],   
# "age":[28,34],
# "name":["ankit","1\2/\3ankitsingh"]}
# # json_str = json.loads(json_string)
# new_json_str = r'json_str'
# new_json = json.dumps(json_string)
# df = pd.read_json(new_json)
# new_string = json_string['name'][0].startswith('anki')
# print(new_string)
import datetime 
# import datetime
record = {
  "BrandName": "Jared",
  "CreatedBy": "AkronPOS",
  "CreatedDate": "2021-08-02T17:23:41.363",
  "CrmcustomerId": "null",
  "CurrentStatus": "Active",
  "DynamicProperties": [
    {
      "propertyName": "REPLACED_Amount",
      "propertyValue": 95.93
    },
    {
      "propertyName": "REPLACED_brandName",
      "propertyValue": "ZalesOutlet"
    },
    {
      "propertyName": "REPLACED_merchLineSeqNum",
      "propertyValue": "1"
    },
    {
      "propertyName": "REPLACED_merchQuantitySeqNum",
      "propertyValue": "1"
    },
    {
      "propertyName": "REPLACED_merchRegisterNum",
      "propertyValue": "3"
    },
    {
      "propertyName": "REPLACED_merchReplacedDate",
      "propertyValue": "2021-7-21"
    },
    {
      "propertyName": "REPLACED_merchStoreNum",
      "propertyValue": "0523"
    },
    {
      "propertyName": "REPLACED_merchTransactionNum",
      "propertyValue": "000005843893"
    }
  ],
  "ExternalContractId": "B726GANS0C$$",
  "Jcid": "null",
  "LimitOfLiability": 1499.99,
  "MerchLineSeqNum": 5,
  "MerchPrice": 1499.99,
  "MerchRegisterNum": "null",
  "MerchSku": "960796706",
  "MerchSoldDate": "2021-08-02T00:00:00",
  "MerchStoreNum": "9980",
  "MerchTax": 0,
  "MerchTransactionNum": "22578",
  "PriceTierId": 2701,
  "PurchaserFirstName": "APPROVE",
  "PurchaserLastName": "RGZWGK",
  "ReturnAmount": "null",
  "ReturnDate": "null",
  "ReturnLineSeqNum": "null",
  "ReturnRegisterNum": "null",
  "ReturnStoreNum": "null",
  "ReturnTransactionNum": "null",
  "Statuses": [
    {
      "CreatedDate": "2021-08-02T17:23:41.37",
      "CrossRefStatusId": 66327615,
      "Description": "Active",
      "StatusId": 7
    }
  ],
  "TotalAmountClaimed": "null",
  "TotalDeductible": 0,
  "UpdatedBy": "AkronPOS",
  "UpdatedDate": "2021-08-02T23:01:17.583",
  "ValidFrom": "2021-08-02T00:00:00",
  "ValidTo": "2120-08-02T00:00:00",
  "VendorComments": "null",
  "VendorContractId": "null",
  "WarranteeAddressLine1": "123900 MONTANA",
  "WarranteeAddressLine2": "null",
  "WarranteeCity": "EL PASO",
  "WarranteeCountry": "US",
  "WarranteeFirstName": "TONY",
  "WarranteeLastName": "BARRENADA",
  "WarranteePhone": "9152151430",
  "WarranteeEmail": "ABARRENADA@GMAIL.COM",
  "WarranteeState": "TX",
  "WarranteeZip": "79925",
  "WarrantyContractId": 41654649,
  "WarrantyPlanCode": "BPP",
  "WarrLineSeqNum": "null",
  "WarrPrice": 209.98,
  "WarrRegisterNum": "null",
  "WarrSku": "null",
  "WarrStoreNum": "9980",
  "WarrTax": 0,
  "WarrTransactionDate": "2021-08-02T00:00:00",
  "WarrTransactionNum": "22578",
  "WarrantyDocumentUrl": "https://signettar-test.jewels.com/api/v1/content/contentstream/rjP2I2W8GuKrs8QoEy-12ZrchIwVpEazzuCzQ88aGAr3!4gciaZ5zS5k5PQvBt-z2!6EIaL15HuBGu5!5JqtiA==/?productProperties=eyJEb2NUeXBlIjoiQlBQIiwiVHJhbnNhY3Rpb25EYXRlVGltZSI6IjA4LzAyLzIwMjEgMDA6MDA6MDAiLCJCcmFuZCI6IkphcmVkIiwiU3RhdGVPclByb3ZpbmNlIjoiVFgiLCJXYXJyYW50eU51bWJlciI6IkI3MjZHQU5TMEMkJCIsIkN1c3RvbWVyRmlyc3ROYW1lIjoiVE9OWSIsIkN1c3RvbWVyTGFzdE5hbWUiOiJCQVJSRU5BREEiLCJDdXN0b21lckFkZHJlc3MxIjoiMTIzOTAwIE1PTlRBTkEiLCJDdXN0b21lckFkZHJlc3NDaXR5IjoiRUwgUEFTTyIsIkN1c3RvbWVyQWRkcmVzc1N0YXRlT3JQcm92aW5jZSI6IlRYIiwiQ3VzdG9tZXJBZGRyZXNzUG9zdGFsQ29kZSI6Ijc5OTI1IiwiQ3VzdG9tZXJQcmltYXJ5UGhvbmUiOiIoOTE1KSAyMTUtMTQzMCIsIk1lcmNoYW5kaXNlU0tVIjoiOTYwNzk2NzA2IiwiTWVyY2hhbmRpc2VQcmljZVBhaWQiOiIxNDk5Ljk5IiwiTWVyY2hhbmRpc2VEZXNjcmlwdGlvbiI6IjEwV0cgRkFTSElPTiBHRU5UUyBSRyIsIlNhbGVCdXNpbmVzc2RhdGUiOiIwOC8wMi8yMDIxIDAwOjAwOjAwIiwiU2FsZVRyYW5zYWN0aW9uc2VxdWVuY2UiOiIyMjU3OCIsIlN0b3JlSWQiOiI5OTgwIn0=",
  "MerchQuantitySequence": 0
}
# for record in event['Records']:
        #Kinesis data is base64 encoded so decode here
        
        #req=base64.b64decode(record["Data"])#.decode("utf-8")
        
        #req=base64.b64decode(record["kinesis"]["data"])#.decode("utf-8")
        #data = json.loads(req)
        
        #data = record["kinesis"]["data"]
data = record
# print("Decoded payload: " + str(data))

#Target columns in Warranty_Contact_Status table

warranty_contract_status_id = 0               #not avaiable in source field
#n3_WarrantyContractStatusId = data['WarrantyContractStatusId']
n3_WarrantyContractId = data['WarrantyContractId']
n3_StatusId = data['Statuses'][0]['StatusId']
n3_CreatedDate = data['CreatedDate']+'Z'

n3_RecSrc = 'WSOR_WARRANTY_CONTRACT_API'
n3_RecSrcTbl = 'API'
n3_LoadDts = str(datetime.datetime.now())[:10] + 'T' + str(datetime.datetime.now())[11:] + 'Z'
n3_SrcDelFlg = 'N'
n3_CurrFlg = 'Y'

warr_contract_status_df = {'prim_key' : '', 'warranty_contract_status_id': 0, 'warranty_contract_id': n3_WarrantyContractId, 'status_id': n3_StatusId, 'created_date': str(n3_CreatedDate), 'cdc_key' : '', 'rec_src' : n3_RecSrc, 'rec_src_tbl' : n3_RecSrcTbl, 'load_dts' : n3_LoadDts, 'src_del_flg' : n3_SrcDelFlg, 'curr_flg' : n3_CurrFlg, 'year' : '', 'month' : '', 'day' : '', 'hour' : ''}
# print(warr_contract_status_df)

#Target columns in Warranty_Contact_Property table

n3_WarrantyContractPropertyId = data['DynamicProperties'][0]['WarrantyContractPropertyId']

n3_WarrantyContractId = data['WarrantyContractId']

# n3_PropertyName = 
# print(data['DynamicProperties'][0]['propertyName'])
n3_PropertyList = []
n3_PropertyName_list = []
n3_PropertyValue_list = []
for i in range(len(data['DynamicProperties'])):
    if data['DynamicProperties'][i]['propertyName'].startswith('REPLACED_'):
        n3_PropertyName =  data['DynamicProperties'][i]['propertyName']
        n3_PropertyValue = data['DynamicProperties'][i]['propertyValue']
    elif data['DynamicProperties'][i]['propertyName'].startswith('TradeIn_'):
        n3_PropertyName =  data['DynamicProperties'][i]['propertyName']
        n3_PropertyValue = data['DynamicProperties'][i]['propertyValue']
    n3_PropertyName_list.append(n3_PropertyName)
    n3_PropertyValue_list.append(n3_PropertyValue)
    n3_PropertyList.append((n3_PropertyName,n3_PropertyValue))
    print(n3_PropertyName,n3_PropertyValue,end = "")
    
# n3_PropertyValue = data['DynamicProperties'][0]['PropertyValue']
n3_IsDeleted = data['DynamicProperties'][0]['IsDeleted']

warr_contract_property_df = {'prim_key' : '', 'warranty_contract_property_id': n3_WarrantyContractPropertyId, 'warranty_contract_id': n3_WarrantyContractId, 'property_name': n3_PropertyName, 'property_value': n3_PropertyValue, 'is_deleted': str(n3_IsDeleted), 'cdc_key' : '', 'rec_src' : n3_RecSrc, 'rec_src_tbl' : n3_RecSrcTbl, 'load_dts' : n3_LoadDts, 'src_del_flg' : n3_SrcDelFlg, 'curr_flg' : n3_CurrFlg, 'year' : '', 'month' : '', 'day' : '', 'hour' : ''}
print(f'printing warr_contract_property_df ')
# print(warr_contract_property_df)

#Target columns in Warranty_Contract table

n3_WarrantyContractId = data['WarrantyContractId']
n3_ExternalContractId = data['ExternalContractId']
n3_VendorContractId = data['VendorContractId']
n3_WarrantyPlanCode = data['WarrantyPlanCode']  #since, WarrantyPlanId is not in json
n3_PriceTierId = data ['PriceTierId']

n3_CrmCustomerId = data['CrmcustomerId']
n3_PurchaserFirstName = data['PurchaserFirstName']
n3_PurchaserLastName = data['PurchaserLastName']
n3_WarranteeFirstName = data['WarranteeFirstName']
n3_WarranteeLastName = data['WarranteeLastName']
n3_WarranteeEmail = data['WarranteeEmail']

n3_WarrTransactionNum = data['WarrTransactionNum']
n3_WarrTransactionDate = data['WarrTransactionDate']+'Z'
n3_WarrStoreNum = data['WarrStoreNum']
n3_WarrSku = data['WarrSku']
n3_WarrRegisterNum = int(0 if data['WarrRegisterNum'] is None else data['WarrRegisterNum'])

n3_WarrLineSeqNum = data['WarrLineSeqNum']
n3_WarrPrice = data['WarrPrice']
n3_WarrTax = data['WarrTax']

n3_MerchTransactionNum = data['MerchTransactionNum']
n3_MerchSoldDate = data['MerchSoldDate']+'Z'
n3_MerchStoreNum = data['MerchStoreNum']
n3_MerchRegisterNum = int(0 if data['MerchRegisterNum'] is None else data['MerchRegisterNum'])
n3_MerchLineSeqNum = data['MerchLineSeqNum']
n3_MerchRetailPrice = data['MerchPrice']  #some doubt as merchretailprice not in JSON
n3_MerchSku = data['MerchSku']

n3_ReturnTransactionNum = data['ReturnTransactionNum']
n3_ReturnDate = (data['ReturnDate'] if data['ReturnDate'] is None else data['ReturnDate']+'Z')
n3_ReturnStoreNum = data['ReturnStoreNum']
n3_ReturnLineSeqNum = int(0 if data['ReturnLineSeqNum'] is None else data['ReturnLineSeqNum'])
n3_ReturnAmount = float(0.0 if data['ReturnAmount'] is None else data['ReturnAmount'])

n3_LimitOfLiability = data['LimitOfLiability']
n3_TotalDeductible = data['TotalDeductible']
n3_ValidFrom = data['ValidFrom']+'Z'
n3_ValidTo = data['ValidTo']+'Z'
n3_CreatedBy = data['CreatedBy']
n3_CreatedDate = (data['CreatedDate'] if data['CreatedDate'] is None else data['CreatedDate']+'Z')
n3_UpdatedBy = data['UpdatedBy']
n3_UpdatedDate = (data['UpdatedDate'] if data['UpdatedDate'] is None else data['UpdatedDate']+'Z')

n3_BrandName = data['BrandName']
n3_Jcid = int(0 if data['Jcid'] is None else data['Jcid'])
n3_MerchTax  = data['MerchTax']
n3_ReturnRegisterNum = data['ReturnRegisterNum']
n3_VendorComments = data['VendorComments']

n3_WarranteeAddressLine1 = data['WarranteeAddressLine1']
n3_WarranteeAddressLine2 = data['WarranteeAddressLine2']
n3_WarranteeCity = data['WarranteeCity']
n3_WarranteeCountry = data['WarranteeCountry']
n3_WarranteePhone = data['WarranteePhone'] if data['WarranteePhone'] is None else int(data['WarranteePhone'])
n3_WarranteeState = data['WarranteeState']
n3_WarranteeZip = data['WarranteeZip']

#Newly added columns
n3_WarrantyDocumentUrl = data['WarrantyDocumentUrl']
n3_MerchQuantitySequence = data['MerchQuantitySequence']

warr_contract_df = {'prim_key' : '', 'warranty_contract_id': n3_WarrantyContractId, 'external_contract_id': n3_ExternalContractId, 'vendor_contract_id': str(n3_VendorContractId), 
    'warranty_plan_cd': n3_WarrantyPlanCode, 'price_tier_id': n3_PriceTierId, 'verbiage_id' : 0, 'crm_customer_id': str(n3_CrmCustomerId), 'purchaser_first_name': n3_PurchaserFirstName,
        'purchaser_last_name': n3_PurchaserLastName, 'warrantee_first_name': n3_WarranteeFirstName, 'warrantee_last_name': n3_WarranteeLastName, 'warrantee_email': str(n3_WarranteeEmail),
            'warr_transaction_num': str(n3_WarrTransactionNum), 'warr_transaction_date': n3_WarrTransactionDate, 'warr_store_num': n3_WarrStoreNum, 'warr_sku': n3_WarrSku, 'warr_register_num': n3_WarrRegisterNum,
                'warr_line_seq_num': n3_WarrLineSeqNum, 'warr_price': n3_WarrPrice, 'warr_tax': n3_WarrTax, 'merch_transaction_num': n3_MerchTransactionNum, 'merch_sold_date': n3_MerchSoldDate, 'merch_store_num': n3_MerchStoreNum,
                    'merch_register_num': n3_MerchRegisterNum, 'merch_line_seq_num': n3_MerchLineSeqNum, 'merch_retail_price': n3_MerchRetailPrice, 'merch_sku': n3_MerchSku, 'return_transaction_num': str(n3_ReturnTransactionNum), 'return_date': n3_ReturnDate,
                        'return_store_num': str(n3_ReturnStoreNum), 'return_line_seq_num': n3_ReturnLineSeqNum, 'return_amount': n3_ReturnAmount, 'limit_of_liability': n3_LimitOfLiability, 'total_deductibile': n3_TotalDeductible, 'valid_from': n3_ValidFrom,
                            'valid_to': n3_ValidTo, 'created_by': n3_CreatedBy, 'created_date': n3_CreatedDate, 'updated_by': str(n3_UpdatedBy), 'updated_date': n3_UpdatedDate, 'cdc_key' : '', 'rec_src' : n3_RecSrc, 'rec_src_tbl' : n3_RecSrcTbl, 'load_dts' : n3_LoadDts, 'src_del_flg' : n3_SrcDelFlg, 'curr_flg' : n3_CurrFlg, 'brand_name': n3_BrandName, 'jcid': n3_Jcid, 'merch_tax': n3_MerchTax,
                                'return_register_num': str(n3_ReturnRegisterNum), 'vendor_comments': str(n3_VendorComments), 'warrantee_address_line1': n3_WarranteeAddressLine1, 'warrantee_address_line2': n3_WarranteeAddressLine2, 'warrantee_city': n3_WarranteeCity,
                                    'warrantee_country': n3_WarranteeCountry, 'warrantee_phone': n3_WarranteePhone, 'warrantee_state': n3_WarranteeState, 'warrantee_zip': n3_WarranteeZip,
                                        'warranty_document_url': n3_WarrantyDocumentUrl, 'merch_quantity_sequence': str(n3_MerchQuantitySequence), 'year' : '', 'month' : '', 'day' : '', 'hour' : ''}

print(warr_contract_df)
