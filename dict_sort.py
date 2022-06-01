#!/usr/bin/env python3

# mydict_1 = {'key5': 'value5', 'key3': 'value3', 'key1': 'value1', 'key2': 'value2'}

# # Create new dictionary
# new_dict = {}

# # sort the keys and store them in a new variable
# sorted_value = sorted(mydict_1.keys())

# # for all the values in sorted_value
# for i in sorted_value:
#    # match the key element with un-sorted dictionary
#    for key, value in mydict_1.items():
#        if key == i:
#           # when matched place the key and value in the new dict
#            new_dict[key] = value

# print(new_dict)

#### Using Lambda ####

mydict = {'key5': 'value4', 'key3': 'value2', 'key1': 'value5', 'key2': 'value1'}

print('Without sort: ', mydict)

# Sort based on item[0] i.e. key in the dictionary
sorted_mydict = dict(sorted(mydict.items(), key=lambda item: item[0]))
print('After sort: ', sorted_mydict)

# Check type of the new dictionary
print(type(sorted_mydict))