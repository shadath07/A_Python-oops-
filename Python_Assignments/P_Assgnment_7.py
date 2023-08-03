# classes : -------------------------------------------------------------------------------------------->

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

# class Student(Person):
#       def __init__(self, fname, lname):
#     super().__init__(fname, lname)


# 1) Write a python class to convert an integer into a roman numeral and viceversa

# import roman
# class romanconverter:
#     def int_roman(self, num):
#         return roman.toRoman(num)
#     def roman_int(self,roman_num):
#         return roman.fromRoman(roman_num)
    
# converter = romanconverter()

# integer = 10
# x = converter.int_roman(integer)
# print(f'{integer} as roman is : {x}')

# roman_num = 'MMXXII'
# y = converter.roman_int(roman_num)
# print(f'{roman_num} as integer is : {y}')



# 2) Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
# These brackets must be close in the correct order, for example "()" 
# and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid. 

# class validity:
#     def find_validity(x):
#         a= ['()', '{}', '[]'] 
#         while any(i in x for i in a):
#             for j in a:
#                 x = x.replace(j, '') 
#         return not x
# s = input("enter: ")
# print(s, "-", "is balanced" 
#       if validity.find_validity(s) else "is Unbalanced") 

# 3) Write a Python class to get all possible unique subsets 
# from a set of distinct integers Input : [4, 5, 6] Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]] 

# import itertools
# class SubsetGenerator:
#     def __init__(self):
#         pass
#     def get_subsets(self, nums):
#         all_subsets = []
#         for i in range(len(nums) + 1):
#             subsets = itertools.combinations(nums, i)
#             all_subsets.extend(subsets)
#         return [list(subset) for subset in all_subsets]
# subset_generator = SubsetGenerator()
# input_set = [4, 5, 6]
# output_subsets = subset_generator.get_subsets(input_set)
# print(output_subsets)


# 4) Write a Python class to find a pair of elements (indices of the two numbers) 
# from a given array whose sum equals a specific target number. 
# Note: There will be one solution for each input and do not use the same element twice. 
# Input: numbers= [90, 20,10,40,50,60,70], target=50 Output: 3, 4 


# class PairElementFinder:
#     def find_indices(self, numbers, target):
#         num_to_index = {}  
#         for index, num in enumerate(numbers):
#             complement = target - num
#             if complement in num_to_index:
#                 return num_to_index[complement], index
#             num_to_index[num] = index
#         return None
# pair_finder = PairElementFinder()
# numbers = [90, 20, 10, 40, 50, 60, 70]
# target = 50
# indices = pair_finder.find_indices(numbers, target)
# print(indices)


# 5) Write a Python class to find the three elements that sum to zero from a set of n real numbers. 
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10] Output : [[-10, 2, 8], [-7, -3, 10]] 

# from itertools import combinations
# class ThreeSumFinder:
#     def three_sum_zero(self, nums):
#         return [[x, y, z] for x, y, z in combinations(nums, 3) if x + y + z == 0]
# input_array = [-25, -10, -7, -3, 2, 4, 8, 10]
# sum_finder = ThreeSumFinder()
# output = sum_finder.three_sum_zero(input_array)
# print(output) 


# 6) Write a Python class to implement pow(x, n) 

# class pow:
#     def pow_number(self,x, n):
#         res = x ** n
#         return res
    
# converter = pow()
# x = int(input("enter the number:"))
# n = int(input("enter the power of the number:"))
# result = converter.pow_number(x, n)
# print(result)


# 7) Write a Python class to reverse a string word by word. 
# Input string : 'hello .py' Expected Output : '.py hello' 

# class reverse_string:
#     def string(self,str):
#         word = str.split()
#         reverse_str = " ".join(reversed(word))
#         return reverse_str
# convert = reverse_string()
# str = "hello .py"
# res = convert.string(str)
# print(res)


# 8) Write a python class which has 2 methods get_string and print_string. 
# get_string takes a string from the user and print_string prints the string in reverse order 

# class Two_method:
#     def get_string(self):
#         self.str = input("enter the string:")
#     def print_string(self):
#         return self.str[::-1]
# convert = Two_method()
# convert.get_string()
# res = convert.print_string()
# print(res)


# 9) Write a Python class named Circle constructed by a radius and 
# two methods which will compute the area and the perimeter of a circle. 


# class circle_radius:
#     def __init__(self, r):
#         self.r = r
#         self.pi = 3.14
#     def circle_area(self):
#         area = self.pi* self.r * self.r 
#         return area
#     def circle_perimeter(self):
#         perimeter = 2 * self.pi * self.r 
#         return perimeter
# radius = 5
# convert = circle_radius(radius)
# area = convert.circle_area()
# perimeter = convert.circle_perimeter()
# print("area of the circle is:",area)
# print("perimeter of the circle is:",perimeter)


# 10) Write a Python program to get the class name of an instance in Python.

# class Student:
#     pass
# p1 = Student()
# res = type(p1).__name__
# print("the instance of the class name:",res)


# Lambda functions------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>

# 1) Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
# also create a lambda function that multiplies argument x with argument y and print the result.Sample Output: 25 48 


# x = lambda a:a+15
# y = lambda b:b*15
# a=5
# b=6
# print(x(a))
# print(y(b))

# 2) Write a Python program to sort a list of tuples using Lambda. 
# Original list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

# x = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# sorted_x = sorted(x, key=lambda x: x[1])
# print(sorted_x)

# 3) Write a Python program to sort a list of dictionaries using Lambda. 
# Original list of dictionaries : [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
# {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}] 
# Sorting the List of dictionaries : [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
# {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}] 

# x = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
# {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}] 
# sorted_x = sorted(x, key=lambda d:d['make'])
# print(sorted_x)


# 4) Write a Python program to find if a given string starts with a given character using Lambda.

# lambda_input = lambda string,i : string.startswith(i)
# str = input("enter the string:")
# ch = input("enter the character to check:")
# res = lambda_input(str,ch)
# print(res)

# 5) Write a Python program to check whether a given string is number or not using Lambda. 

# str_key = lambda x:x.isdigit()
# str_input = input("enter the string:")
# res = str_key(str_input)
# print(res)

# 6)  Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda 
# Orginal list: [19, 65, 57, 39, 152, 639, 121, 44, 90, 190] 
# Numbers of the above list divisible by nineteen or thirteen: [19, 65, 57, 39, 152, 190] 

# num = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# res = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, num))
# print(res)

# 7) Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda. 
# Original Matrix: [[1, 2, 3], [2, 4, 5], [1, 1, 1]] 
# Sort the said matrix in ascending order according to the sum of its rows [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
#  Original Matrix: [[1, 2, 3], [-2, 4, -5], [1, -1, 1]] 
# Sort the said matrix in ascending order according to the sum of its rows [[-2, 4, -5], [1, -1, 1], [1, 2, 3]] 

# x =  [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# y = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# res_x = sorted(x, key=lambda x: x)
# res_y = sorted(y, key=lambda y: y)
# print(res_x)
# print(res_y)

# 8) Write a Python program to check whether a given string contains a capital letter, a lower case letter, 
# a number and a minimum length using lambda. Minimum length : 10 input string: PaceWisd0m o/p: valid string 


# check_valid_string = lambda string: all(c.isupper() or c.islower() or c.isdigit() for c in string) and len(string) >= 10
# input_string = "PaceWisd0m"
# result = "valid string" if check_valid_string(input_string) else "invalid string"
# print(result)

# 9) Write a Python program to find the elements of a given list of strings that contain specific substring using lambda. 
# Original list: ['red', 'black', 'white', 'green', 'orange'] 
# Substring to search: ack Elements of the said list that contain specific substring: ['black'] 
# Substring to search: abc Elements of the said list that contain specific substring: []


# x = ['red', 'black', 'white', 'green', 'orange']
# substring = input("enter the substring to search:")
# filter_substring = lambda lst, sub: list(filter(lambda x: sub in x, lst))
# result = filter_substring(x, substring)
# print("Substring to search:", substring)
# print("Elements of the said list that contain specific substring:", result)


# 10) Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings. 
# Original list: [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1] 
# Sort the said mixed list of integers and strings: [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']

# x = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1] 
# res = sorted(x, key=lambda a:(isinstance(a, str) , a))
# print(res)







