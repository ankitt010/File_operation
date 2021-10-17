from pandas.core.reshape.concat import concat


try:
    from logging import error
    import pandas as pd
    import datetime
    from zipfile import ZipFile
    import zipfile
    from pandas.core.indexes.base import Index
    from io import BytesIO
except Exception as e:
    print(e)
 
# reading data from Target_Headcount_by_Store_by_Wk into pandas 
try:
    df = pd.read_csv(r"C:\Users\ankit.chandel\Downloads\Target_Headcount_by_Store_by_Wk (1).csv", skip_blank_lines=True)
    # df_null = df[df.isna().any(axis=1)]
    # print(df_null)
except FileNotFoundError as e:
    print(e)
# print(df)
try:
    # finding rows which have any null values
    df_null = df[df.isna().any(axis=1)]
    print(df_null)
    # droping rows which contain any null values 
    df = df.dropna(how='any',axis=0) 
    column_list = ['Week Ending Date', 'Store Number', 'Support Center',
        'Target Headcount']
    duplicates_df = pd.DataFrame(columns=column_list)

    duplicates_df = df[df.duplicated(keep="first")]
    # new_df = pd.DataFrame(columns=column_list)
    df = df.drop_duplicates(keep="first")

    # new_df = new_df.append(duplicates_df)
    prev_len = duplicates_df.shape[0]
    print(duplicates_df)
    duplicates_df = pd.concat([duplicates_df,df_null])
    print('combined df',duplicates_df)

    for column in duplicates_df.columns:
        duplicates_df[column] = duplicates_df[column].astype(str)
    # new_df  = new_df.applymap(str)
    column_names = ['file_Name','error_data','error_message','run_date']

    error_df = pd.DataFrame(columns =column_names)
    print(error_df)
    duplicates_df = duplicates_df.reset_index(drop = True)
    print(duplicates_df)
    for i,j in zip(range(error_df.shape[0],duplicates_df.shape[0]+error_df.shape[0]),range(duplicates_df.shape[0])):
        if (True in  list(duplicates_df.loc[j,:] == 'nan')) or (duplicates_df.loc[j,:].isna().any()):
            error_df.at[i,'error_message'] = 'rows contain null values'
        else:
            # print(duplicates_df.loc[j,:].isna().any())
            error_df.at[i,'error_message'] = 'rows are duplicate based on all columns'
        error_df.at[i,'file_name'] = 'Target_Headcount_by_Store_by_Wk (1).csv'
        error_df.at[i,'error_data'] = duplicates_df.loc[i,:]
        error_df.at[i,'run_date'] = datetime.datetime.now()
    print(error_df)

    # error_df['error_data'] = new_df.loc[:,:]
    # find duplicates if key matches
    duplicate_by_key_df = pd.DataFrame()
    duplicate_by_key_df = df[df.duplicated(subset=['Week Ending Date', 'Store Number', 'Support Center'],keep='first')]
    print(f'these rows are duplicates based on key {duplicate_by_key_df}')
    df = df.drop_duplicates(subset=['Week Ending Date', 'Store Number', 'Support Center'])

    # column_names = ['file_Name','error_data','error_message','run_date']
    # error_df = pd.DataFrame(columns =['file_Name','error_data','error_message','run_date'])
    # duplicate_by_key_df = pd.concat(duplicate_by_key_df,df_null)
    len_df = duplicate_by_key_df.shape[0]

    for column in duplicate_by_key_df.columns:
        duplicate_by_key_df[column] = duplicate_by_key_df[column].astype(str)

    print(duplicate_by_key_df)
    duplicate_by_key_df = duplicate_by_key_df.reset_index(drop = True)
    print(duplicate_by_key_df.shape[0])
    
    # while duplicate_by_key_df.shape[0]:
    # for j in range(duplicate_by_key_df.shape[0]):
    for i,j in zip(range(error_df.shape[0],error_df.shape[0] + duplicate_by_key_df.shape[0]),range(duplicate_by_key_df.shape[0])):
        error_df.at[i,'file_name'] = 'Target_Headcount_by_Store_by_Wk (1).csv'
        error_df.at[i,'error_data'] = duplicate_by_key_df.loc[j,:]
        error_df.at[i,'error_message'] = 'rows are duplicate based on key fields'
        error_df.at[i,'run_date'] = datetime.datetime.now()
    print(error_df,'after one file')
    print(error_df)
    error_df.to_csv('logging.csv')
except Exception as e:
    print(e)
# reading data from Target_Headcount_by_Store_by_Wk into pandas 
try:
    df = pd.read_csv(r"C:\Users\ankit.chandel\Downloads\Store_Weekly_Dollar_Budget.csv", skip_blank_lines=True)
    # print(df)
except FileNotFoundError as e:
    print(e)

try:
    # finding rows which have any null values
    df_null = df[df.isna().any(axis=1)]
    print(df_null)
    # droping rows which contain any null values 
    df = df.dropna(how='any',axis=0) 
    column_list  = df.columns
    duplicates_df = pd.DataFrame(columns=column_list)

    duplicates_df = df[df.duplicated(keep="first")]
    # new_df = pd.DataFrame(columns=column_list)
    df = df.drop_duplicates(keep="first")

    # new_df = new_df.append(duplicates_df)
    prev_len = duplicates_df.shape[0]

    # new_df = new_df.to_string(header=False,index=False)
    duplicates_df = pd.concat([duplicates_df,df_null])
    for column in duplicates_df.columns:
        duplicates_df[column] = duplicates_df[column].astype(str)
    # new_df  = new_df.applymap(str)
    column_names = ['file_Name','error_data','error_message','run_date']

    # error_df = pd.DataFrame(columns =column_names)
    new_df = duplicates_df.reset_index(drop = True)
    for i,j in zip(range(error_df.shape[0],error_df.shape[0] + duplicates_df.shape[0]),range(duplicates_df.shape[0])):
        if (True in  list(duplicates_df.loc[j,:] == 'nan')) or (duplicates_df.loc[j,:].isna().any()):
            error_df.at[i,'error_message'] = 'rows contain null values'
        else:
            error_df.at[i,'file_name'] = 'Store_Weekly_Dollar_Budget.csv'
            error_df.at[i,'error_data'] = new_df.loc[j,:]
            error_df.at[i,'error_message'] = 'rows are duplicate based on all columns'
            error_df.at[i,'run_date'] = datetime.datetime.now()

    # error_df['error_data'] = new_df.loc[:,:]


    # find duplicates if key matches
    duplicate_by_key_df = pd.DataFrame()
    duplicate_by_key_df = df[df.duplicated(subset=['Week Ending Date', 'Store Number', 'Support Center'],keep='first')]
    print(f'these rows are duplicates based on key {duplicate_by_key_df}')
    df = df.drop_duplicates(subset=['Week Ending Date', 'Store Number', 'Support Center'])

    # column_names = ['file_Name','error_data','error_message','run_date']
    # error_df = pd.DataFrame(columns =['file_Name','error_data','error_message','run_date'])
    len_df = duplicate_by_key_df.shape[0]

    for column in duplicate_by_key_df.columns:
        duplicate_by_key_df[column] = duplicate_by_key_df[column].astype(str)

    # print(duplicate_by_key_df)
    duplicate_by_key_df = duplicate_by_key_df.reset_index(drop = True)

    # while duplicate_by_key_df.shape[0]:
    # for j in range(duplicate_by_key_df.shape[0]):
    for i,j in zip(range(error_df.shape[0],error_df.shape[0] + len_df),range(len_df)):
        error_df.at[i,'file_name'] = 'Store_Weekly_Dollar_Budget.csv'
        error_df.at[i,'error_data'] = duplicate_by_key_df.loc[j,:]
        error_df.at[i,'error_message'] = 'rows are duplicate based on key fields'
        error_df.at[i,'run_date'] = datetime.datetime.now()
    print(error_df,'weelkybudget and target_headcount')
except Exception as e:
    print(e)

try:
    df = pd.read_csv(r'C:\Users\ankit.chandel\Downloads\PTO_Budget_Hours_&_Dollars.csv')
except FileNotFoundError as e:
    print(e)
try:
    # finding rows which have any null values
    df_null = df[df.isna().any(axis=1)]
    print(df_null)
    # droping rows which contain any null values 
    df = df.dropna(how='any',axis=0) 
    column_names = ['file_Name','error_data','error_message','run_date']
    # error_df = pd.DataFrame(columns=column_names)
    column_list = df.columns
    print(column_list)
    duplicates_df = df[df.duplicated(keep="first")]
    new_df = pd.DataFrame(columns=column_list)
    df = df.drop_duplicates(keep="first")

    # new_df = new_df.append(duplicates_df)
    prev_len = duplicates_df.shape[0]
    print('duplicate based on all columns',duplicates_df)

    error_df_len = error_df.shape[0]
    # new_df = new_df.to_string(header=False,index=False)
    duplicates_df = pd.concat([duplicates_df,df_null])
    for column in new_df.columns:
        duplicates_df[column] = duplicates_df[column].astype(str)
    duplicates_df = duplicates_df.reset_index(drop=True)

    for i,j in zip(range(error_df.shape[0],error_df.shape[0] + prev_len),range(duplicates_df.shape[0])):
        if (True in  list(duplicates_df.loc[j,:] == 'nan')) or (duplicates_df.loc[j,:].isna().any()):
            error_df.at[i,'error_message'] = 'rows contain null values'
        else:
            error_df.at[i,'file_name'] = 'PTO_Budget_Hours_&_Dollars.csv'
            error_df.at[i,'error_data'] = duplicates_df.loc[j,:]
            error_df.at[i,'error_message'] = 'rows are duplicate based on all columns'
            error_df.at[i,'run_date'] = datetime.datetime.now()
    print(error_df,'after fetching duplicate')


    # error_df['error_data'] = new_df.loc[:,:]
    # find duplicates if key matches
    column_list = ['Fiscal Year', 'Fiscal Month Number', 'Banner', 'PTO Budget Hours',
        'PTO Budget Dollars']
    duplicate_by_key_df = pd.DataFrame()
    duplicate_by_key_df = df[df.duplicated(subset=['Fiscal Year', 'Fiscal Month Number', 'Banner'],keep='first')]
    print(f'these rows are duplicates based on key {duplicate_by_key_df}')
    df = df.drop_duplicates(subset=['Fiscal Year', 'Fiscal Month Number', 'Banner'])

    # column_names = ['file_Name','error_data','error_message','run_date']
    # error_df = pd.DataFrame(columns =['file_Name','error_data','error_message','run_date'])
    len_df = duplicate_by_key_df.shape[0]

    for column in duplicate_by_key_df.columns:
        duplicate_by_key_df[column] = duplicate_by_key_df[column].astype(str)

    # print(duplicate_by_key_df)
    duplicate_by_key_df = duplicate_by_key_df.reset_index(drop=True)
    print(duplicate_by_key_df.shape[0])

    for i,j in zip(range(error_df.shape[0],error_df.shape[0] + len_df),range(len_df)):
        error_df.at[i,'file_name'] = 'PTO_Budget_Hours_&_Dollars.csv'
        error_df.at[i,'error_data'] = duplicate_by_key_df.loc[j,:]
        error_df.at[i,'error_message'] = 'rows are duplicate based on key fields'
        error_df.at[i,'run_date'] = datetime.datetime.now()
except Exception as e:
    print(e)

try:
    df  = pd.read_csv(r'C:\Users\ankit.chandel\Downloads\Budget_Wage_Rt_Banner_by_Month.csv',skip_blank_lines=True)
except FileNotFoundError as e:
    print(e)

try:
    # finding rows which have any null values
    df_null = df[df.isna().any(axis=1)]
    print(df_null)
    # droping rows which contain any null values 
    df = df.dropna(how='any',axis=0) 
    column_list = df.columns
    print(column_list)
    duplicates_df = df[df.duplicated(keep="first")]
    new_df = pd.DataFrame(columns=column_list)
    df = df.drop_duplicates(keep="first")

    # new_df = new_df.append(duplicates_df)
    prev_len = duplicates_df.shape[0]
    print('duplicate based on all columns',duplicates_df)
    # new_list = []
    # new_df = new_df.reset_index()

    error_df_len = error_df.shape[0]
    # new_df = new_df.to_string(header=False,index=False)
    duplicates_df = pd.concat([duplicates_df,df_null])
    for column in new_df.columns:
        duplicates_df[column] = duplicates_df[column].astype(str)
    duplicates_df = duplicates_df.reset_index(drop=True)
    # print(duplicate_by_key_df)
    # print(duplicates_df.loc[0,:])
    # new_df  = new_df.applymap(str)
    # column_names = ['file_Name','error_data','error_message','run_date']

    # error_df = pd.DataFrame(columns =['file_Name','error_data','error_message','run_date'])
    # error_df1 = pd.DataFrame(columns=column_names)
    for i,j in zip(range(error_df.shape[0],error_df.shape[0] + prev_len),range(duplicates_df.shape[0])):
        if (True in  list(duplicates_df.loc[j,:] == 'nan')) or (duplicates_df.loc[j,:].isna().any()):
            error_df.at[i,'error_message'] = 'rows contain null values'
        else:
            error_df.at[i,'file_name'] = 'Budget_Wage_Rt_Banner_by_Month.csv'
            error_df.at[i,'error_data'] = duplicates_df.loc[j,:]
            error_df.at[i,'error_message'] = 'rows are duplicate based on all columns'
            error_df.at[i,'run_date'] = datetime.datetime.now()
    print(error_df,'after fetching duplicate')


    # error_df['error_data'] = new_df.loc[:,:]
    # find duplicates if key matches
    column_list = ['Fiscal Year', 'Fiscal MONTH Number', 'Banner',
        'Management Wage Rate Budget', 'Staff Wage Rate Budget']
    duplicate_by_key_df = pd.DataFrame()
    duplicate_by_key_df = df[df.duplicated(subset=['Fiscal Year', 'Fiscal MONTH Number', 'Banner'],keep='first')]
    print(f'these rows are duplicates based on key {duplicate_by_key_df}')
    df = df.drop_duplicates(subset=['Fiscal Year', 'Fiscal MONTH Number', 'Banner'])

    # column_names = ['file_Name','error_data','error_message','run_date']
    # error_df = pd.DataFrame(columns =['file_Name','error_data','error_message','run_date'])
    len_df = duplicate_by_key_df.shape[0]

    for column in duplicate_by_key_df.columns:
        duplicate_by_key_df[column] = duplicate_by_key_df[column].astype(str)

    # print(duplicate_by_key_df)
    duplicate_by_key_df = duplicate_by_key_df.reset_index(drop=True)
    print(duplicate_by_key_df.shape[0])

    for i,j in zip(range(error_df.shape[0],error_df.shape[0] + len_df),range(len_df)):
        error_df.at[i,'file_name'] = 'Budget_Wage_Rt_Banner_by_Month.csv'
        error_df.at[i,'error_data'] = duplicate_by_key_df.loc[j,:]
        error_df.at[i,'error_message'] = 'rows are duplicate based on key fields'
        error_df.at[i,'run_date'] = datetime.datetime.now()

    # print(error_df)
    error_df.to_csv('logging.csv')
except Exception as e:
    print(e)
# archival process for source files

compression = zipfile.ZIP_DEFLATED
current_date = datetime.datetime.now().strftime("%Y%m%d")
try:
    with ZipFile(f'sample.zip{current_date}', 'w') as zipObj:
    # Add multiple files to the zip
        zipObj.write(r'C:\Users\ankit.chandel\Downloads\Budget_Wage_Rt_Banner_by_Month.csv')
        zipObj.write(r'C:\Users\ankit.chandel\Downloads\Store_Weekly_Dollar_Budget.csv')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)


