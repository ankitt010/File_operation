# # def print_weekdays(week_list):
# #     for week in week_list:
# #         yield week


# # week_list = ['mon','tue','wed','thurs','fri','sat','sun']
# # my_num = print_weekdays(week_list)
# # print(my_num)

# # print(next(my_num))
# # print(next(my_num))
# # print(next(my_num))
# # print(next(my_num))
# # print(next(my_num))
# # print(next(my_num))
# # print(next(my_num))

# Input = {'a', 'b', 'c', 'd'}
# demo_list = list(Input)
# # demo_values = [3,2,8,4,7,9,0,4,5,6,7]
# num = 2

# rem = 4
# another_list = []
# new_list = []
# def func(demo_values):
#     if len(demo_values) < rem:
#         new_list.append(demo_values[:])
#         return
#     else:
#         another_list.append(demo_values[:4])
#         func(demo_values[rem:])
# func([3,2,8,4,7,9,0,4,5,6,7])


# print(another_list)
# # Output: {'a':[3,2,8], 'b':[4,7,9], c:[0,4,5], 'd':[6,7]}
# demo_dict = {}
# len_dict = len(demo_values) % num

# if len_dict == 0:
#     for key in demo_list:
#         for values in demo_values:
#             demo_dict[key] = 


# elif len_dict != 0:
#     pass
# for key in Input:
#     print(key)

# yield key word

# Input : {'a', 'b', 'c', 'd'}
# [3,2,8,4,7,9,0,4,5,6,7]
# Output: {'a':[3,2,8], 'b':[4,7,9], c:[0,4,5], 'd':[6,7]}

input = ['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'd', 'a']
Output = ['a', 2, 'b', 4, 'c', 2, 'd', 1, 'a', 1]
output_list = []
count = 1

for num in  range(len(input)-1):
    
    if input[num] == input[num+1]:
        count += 1
    else:
        output_list.append(input[num])
        output_list.append(count)
        count = 1
output_list.append(input[num+1])

output_list.append(count)
print(output_list)






