import pandas as pd
# from srt import error_df,duplicate_by_key,duplicates,duplicates_df,new_df,column_list
df = pd.DataFrame(data={'A': [1, 2, 3], 'B': [1,2,3]})
df['B'] = df['B'].astype('object')
df['A'] = df['A'].astype('object')

# duplicates_df = duplicates_df.drop(columns=column_list)
# duplicates_df.columns = range(duplicates_df.shape[1])
# df = df[:].values
# print(df['A'])
# df = df.drop([0,1])
# print(duplicates_df))
# df.at[1, 'A'] = duplicates_df[0:]
# as.numeric(df[1,])
# for row in duplicates:
#     print(row)
df = df.to_string(header=False,index=False)
# print('printing vl')
# print(df)
# # for row in new_df:
#     print(row[1])
# print(df.loc[1:1])
# df_duplicate = pd.DataFrame(duplicates)
# print(duplicates[0])

# gcd of two numbers
num1 = 150
num2 = 250
gcd_list = []
if num1 <= num2:
    for i in range(2,num1):
        if num1 % i == 0 and num2 % i == 0:
            gcd_list.append(i)
print(gcd_list)
print(max(gcd_list))
from math import ceil, sqrt
n = 97
for i in range(2,3):
    print('okay')
print(ceil(sqrt(2)))
number = 50
fib_list = []
def fib():
    a,b = 0,1
    for _ in range(number):
        # fib_list.append((a,b))
        fib_list.append(a)
        
        yield a
        a,b = b,a+b
    print(fib_list)
        # print(fib_list)
         
print(list(fib()))

# prime_list = []
# for number in range(2,num1):
#     n = number
#     for i in range(2,ceil(sqrt(n))):
#         if n % i == 0:
#             print(n)
#             break
#     else:
#         prime_list.append(n)

        # print('congratulation number is prime',)
        # print(prime_list)
# '''
# string = 'abcdef'
# substring_list = []
# for i in range(len(string)+1):
#     for j in range(i+1,len(string)+1):
#         substring_list.append(string[i:j])
# # substring_list.append(string[-1])
# print(substring_list)
# '''