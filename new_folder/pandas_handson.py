# ***corey pandas***
import json
with open ('s3.json') as f:
    new_string = json.load(f)
with open('claims2.json') as f2:
    new_string2 = json.load(f2)
# for new_list in new_strig:

#     print(new_list)
# print(new_strig)
def sorting(item):
    if isinstance(item, dict):
        return sorted((key, sorting(values)) for key, values in item.items())
    if isinstance(item, list):
        return sorted(sorting(x) for x in item)
    else:
        return item
print(sorting(new_string) == sorting(new_string2))


# parquet schema nikalo and compare karo json se (json to parquet conversion hai wahi na)
# (statuses)
# schema of prquet as input and print the shema
# warranty contract all three tables and claims 

# print(sorting(new_string) == sorting(json2_dict))