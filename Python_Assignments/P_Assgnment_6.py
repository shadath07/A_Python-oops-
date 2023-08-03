# List and Dictionaries---------------------------------------------------------->

# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

# def Ascending_Descending():
#     asc_dict = {}
#     desc_dict = {}
#     my_dict = {
#         "a": '12',
#         "b": '14',
#         "c": '13',
#         "d": '15'
#     }
#     asc_items = sorted(my_dict.items(), key=lambda x: x[1])
#     for key, value in asc_items:
#         asc_dict[key] = value   
#     desc_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
#     for key, value in desc_items:
#         desc_dict[key] = value
#     return asc_dict, desc_dict
# print(Ascending_Descending())

        
# def sort_dictionary_by_value(d):
#     ascending_sorted_dict = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
#     descending_sorted_dict = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
#     return ascending_sorted_dict, descending_sorted_dict
# my_dict = {
#     "a": 12,
#     "b": 13,
#     "c": 14,
#     "d": 15
# }
# asc_dict, desc_dict = sort_dictionary_by_value(my_dict)
# print("Ascending order:", asc_dict)
# print("Descending order:", desc_dict)

# 2. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# dict = {
#     0 : 10,
#     1:20
# }
# dict[2]= 30
# print(dict)

# 3. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# ---------------------------------> by using the ** concatenation operator
# d1={1:10, 2:20}
# d2={3:30, 4:40}
# d3={5:50,6:60}
# res ={**d1, **d2, **d3}
# print(res)


# 4. Write a Python script to check if a given key already exists in a dictionary. 

# def key_check(dict,key):
#     return key in dict
# my_dict = {
#     "a": 12,
#     "b": 13,
#     "c": 14,
#     "d": 15
# }
# key_to_check = input("enter the key to check:")
# if key_check(my_dict, key_to_check):
#     print(f"the key '{key_to_check}' exists in the dictionary.")
# else:
#     print(f"the key '{key_to_check}' not exists in the dictionary.")



# 5. Write a Python program to iterate over dictionaries using for loops.

# def iterate_dictionaries(d):
#     for k,v  in d.items():
#         print(f"'{k}' : '{v}'")
# my_dict = {
#     "a": 12,
#     "b": 13,
#     "c": 14,
#     "d": 15
# }
# print(iterate_dictionaries(my_dict))


# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# def generate_print(n):
#     dict ={}
#     for num in range(1,1+n):
#         dict[num] = num * num
#     return dict
# input = int(input("enter the number:"))
# res = generate_print(input)
# print(res)   


# 7. Write a Python script to merge two Python dictionaries.

# d1 = {
#     "a": "10",
#     "b" : "20"
# }
# d2 = {
#     "c" : "60",
#     "d" : "90"
# }
# res = {**d1, **d2}
# print(res)

# 8.  Write a Python program to sum all the items in a dictionary.

# def sum_dict(dict):
#         return sum(dict.values())
# d = {"a":10,"b":20,"c":30,"d":0}
# print(sum_dict(d))


# 9. Write a Python program to multiply all the items in a dictionary.

# def mult_dict(dict):
#     mult = 1
#     for i in dict:
#         mult = mult* dict[i]
#     return mult
# d = {"a":10,"b":20,"c":30,"d":7}
# res = mult_dict(d)
# print(res)

# 10. Write a Python program to remove a key from a dictionary. 

# input = input("enter the key to remove:")
# d = {"a":10,"b":20,"c":30,"d":7}
# del(d[input])
# print(d)


# 11. Write a Python program to sort a dictionary by key.

# d = {"b":10,"c":20,"d":30,"a":35}
# for key,value in d.items():
#     res = sorted(d.items())
#     print(dict(res))
#     break


# 12. Write a Python program to get the maximum and minimum value in a dictionary. 

# d = {"b":10,"c":20,"d":30,"a":35}
# for key,value in d.items():
#     print(max(d.values()))
#     print(min(d.values()))
#     break


# 13. Write a Python program to remove duplicates from Dictionary.

# d = {"b":10,"c":20,"d":30,"a":35,"b":10,"c":20,"d":30,"a":35}
# for key,value in d.items():
#     res = set(d.items())
# print(dict(res))


# 14. Write a Python program to check a dictionary is empty or not. 

# def empty_Or_not(dict):
#     return not bool(dict)

# d = {}
# if empty_Or_not(d):
#     print("dict is empty")
# else:
#     print("dict is not empty")

# 15. Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


# def combine_dict(d1, d2):
#     combined_dict = {}
#     for key, value in d1.items():
#         combined_dict[key] = value + combined_dict.get(key, 0)
#     for key, value in d2.items():
#         combined_dict[key] = value + combined_dict.get(key, 0)
#     return combined_dict
# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# combined_dict = combine_dict(d1, d2)
# print("Combined Dictionary:", combined_dict)


# 16. Write a Python program to find the highest 3 values in a dictionary.

# def highest_values(d, n):
#     item = sorted(d.items(), key=lambda x: x[1], reverse=True)
#     high_value = [value for key, value in item[:n]]
#     return high_value
# dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
# highest_3_values = highest_values(dict, 3)
# print("Highest 3 values:", highest_3_values)

# 17. Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

# def key_match(d1,d2):
#     for k,v in d1.items():
#         if k in d2 and d2[k] == v:
#             print(f'{k} : {v} is present in both x and y')
#             break
# d1 = {'key1': 1, 'key2': 3, 'key3': 2}
# d2 = {'key1': 1, 'key2': 2}
# res = key_match(d1,d2)
# print(res)

# 18. Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

# def  check_empty(dict):
#     return not bool(dict)

# d = list({})
# if check_empty(d):
#     print("dict is empty")
# else:
#     print("dict is not empty")
# res = check_empty(d)
# print(res)


# 19. Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]


# def remove_duplicates(input_list):
#     x = set()
#     new_list = []
#     for i in input_list:
#         sub_tuple = tuple(i)
#         if sub_tuple not in x:
#             new_list.append(i)
#             x.add(sub_tuple)
#     return new_list
# sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# new_list = remove_duplicates(sample_list)
# print("New List:", new_list)


# 20. Write a Python program to extend a list without append.
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]

# x = [10, 20, 30]
# y = [40, 50, 60]
# x.extend(y)
# print(x)