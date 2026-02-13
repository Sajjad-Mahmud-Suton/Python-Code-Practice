dict1 = {"Sajjad": 85, 
         "Mahmud": 92}
dict2 = {"Suton": 78, 
         "Sajid": 95}

merged_dict = {}

for key in dict1:
    merged_dict[key] = dict1[key]
for key in dict2:
    merged_dict[key] = dict2[key]

print("Merged Dictionary: ",merged_dict)