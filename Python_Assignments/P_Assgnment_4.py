# 1. Write a Python program to calculate the length of a string.



# string = input("enter the string:")
# lenght = len(string)
# print(lenght)


# 2. Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

# def Character_number_count(str):
#     character_count = {}
#     for i in str:
#         if i in character_count:
#             character_count[i] += 1
#         else:
#             character_count[i]  = 1
#     return character_count
# sample_string = input("enter the string:")
# res  = Character_number_count(sample_string)
# print(res)

# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
# Sample String : 'thisisniceone'
# Expected Result : 'thne”'
# Sample String : 'ab'
# Expected Result : 'abab'
# Sample String : 'f'
# Expected Result : Empty String 


# def sample_string(x):
#     for i in x :
#         if len(x) >= 2 :
#             return x[:2] + x[-2:]
#         else:
#             return "Empty"
# input = input("enter the string:")
# res = sample_string(input)
# print(res)


# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

# def replace_occurence(x):   
#     first_word = x[0]
#     replace_word = first_word
#     for i in x[1:]:
#         if i == first_word:
#             replace_word = replace_word + '$'
#         else:
#             replace_word = replace_word + i
#     return replace_word
# sample_input = input("enter the string:")
# res = replace_occurence(sample_input)   
# print(res)


# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'


# first_string = input("enter the string:")
# second_string  = input("enter the string:")
# swap_1 = second_string[:2] + first_string[2]
# swap_2 = first_string[:2] + second_string[2]
# res  = print(f'{swap_1} {swap_2}')
# print(res)


# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing' 
# Sample String : 'string'
# Expected Result : 'stringly'


# def add_string(x):
#     for i in x:
#         if len(x)< 3:
#             return x
#         elif len(x) >= 3 and x[-3:] != 'ing':
#             return x + 'ing'
#         elif x[-3:] == 'ing':
#             return x + 'ly'
#         else:
#             return x
# str = input("enter the string:")
# res = add_string(str)
# print(res)
        
        
# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'


# def apperance_substring(x):
#     str1 = x.find('not')
#     str2 = x.find('poor')
#     if str1 != -1 and str2 != -1 and str1< str2:
#         return x[:str1] + "good" + x[str2 + 4:]
#     else:
#         return x
# input1 = 'The lyrics is not that poor!'
# input2 = 'The lyrics is poor!'
# res1 = apperance_substring(input1)
# res2 = apperance_substring(input2)
# print(res1) 
# print(res2)    


# 8. Write a Python function that takes a list of words and returns the length of the longest one. 


# def list_word(x):
#     max_length = 0
#     for i in x:
#         if len(i) > max_length:
#             max_length = len(i)
#     return max_length
# input = ["apple","banana","graphes","watermelon"]
# res = list_word(input)
# print(res)

# 9. Write a Python program to remove the nth index character from a nonempty string.

# input = input("enter the string:")
# res = input[::-1]
# print(res)


# 10. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white


# list = ["red","white","black","red","green","black"]
# res = set(list)
# print(sorted(res))

# 11. Write a Python function to reverses a string if it's length is a multiple of 4. 

# def reverse_string(x):
#     if len(x) / 4 and len(x) % 4 == 0:
#         return x[::-1]
#     else:
#         return "Not a multiple of 4"
# input = input("enter the string:")
# res = reverse_string(input)
# print(res)


# 12. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

# def String_uppercase(x):
#     upper_case = sum(1 for i in x[:4] if i.isupper())
#     if upper_case >= 2:
#         return x.upper()
#     else:
#         return x
# input = input("enter the string:")
# res = String_uppercase(input)
# print(res)

# 13. Write a Python program to check whether a string starts with specified characters.

# x = input("enter the string:")
# str_character =input("enter the specified character string to be checked:")
# if str_character == x[0]:
#     print("The string starts with specified character")
# else:
#     print("The string does not start with specified character")


# 14. Write a Python program to print the following floating numbers upto 2 decimal places.
# 3.1415926

# f_numbers = 3.1415926----------------------------------------------->using f-string functions
# format_num = f'{f_numbers:.2f}'
# print(format_num)


# num = 3.1415926--------------------------------->>>using format functions
# format_num = '{:.2f}'.format(num)
# print(format_num)


# 15. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

# def repeatedCh_count(x):
#     character_count = {}
#     for i in x:
#         if i in character_count:
#             character_count[i] += 1
#         else:
#             character_count[i] = 1
#     return character_count
# input_str = input("enter the string:")
# res = repeatedCh_count(input_str) 

# sorted_res = sorted(res.items(), key=lambda item:item[1] , reverse = True)

# for char , count in sorted_res:
#     if count > 1:
#         print(f'{char} {count}')


# 16. Write a Python program to print the index of the character in a string.    

# str = input("enter the string:")
# char_str = input("enter the character of the string:")
# res = str.index(char_str)
# print(res)      

# method 1
# str = input("enter the string:")
# for index , char in enumerate(str):
#     print(f"The string character '{char}' is found at : {index}")           

# method 2
# def string_char_index(str): ----------------------------------------------------> by defining a function
#     for index, char in enumerate(str):
#         print(f"Character '{char}' is found at index: {index}")
# input_str = input("Enter the string: ")
# string_char_index(input_str)



# 17. Write a Python program to convert a string in a list.


# str =input("enter the string:")
# res = list(str)
# print(res) 

# def string_convert(x):--------------------------------> dy defining a function
#     for i in range(len(x)):
#         res = list(x)
#     return res
# input_str = input("enter the string:")
# print(string_convert(input_str))

# 18. Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"

# using maketrans() ->it returns translation table using str.transalate()
# translate()---------->This returns a copy of the string where all characters occurring in the optional argument are removed, 
# and the remaining characters have been mapped through the translation table, given by the maketrans table. 
# def replace(str1):------------------------------------->replace . and viceversa
#     maketrans = str1.maketrans
#     res  = str1.translate(maketrans(',.','.,',''))
#     return res.replace(',',',')
# string = input("enter the string:")
# print(replace(string))

# def replace_str(x):
#     arr = []
#     for i in x:
#         if i == ".":
#             arr.append(",")
#         elif i == ",":
#             arr.append(".")
#             continue
#         elif i == " ":
#             continue
#         else:
#             arr.append(i)
#     y = "".join(arr)
#     return y

# input_str = input("enter the string:")
# print(replace_str(input_str))

# 19. Write a Python program to find smallest and largest word in a given string.

# to find the largest and smallest in the single given words
# str = input("enter the string:")
# print("The smallest word string is:",min(str))
# print("The Largest word string is:",max(str))

# to find the small and largest of the string in a given set of  sentences by defining a functions

# def small_Large_string(x):
#     word = x.split()
#     small_word = min(word, key=len)
#     large_word  = max(word, key=len)
#     return small_word, large_word

# input_str = input("enter the string:")
# small,large = small_Large_string(input_str)
# print(f'the smallest word is:{small}')
# print(f'the largest word is:{large}')


# 20. Write a Python program to remove all consecutive duplicates of a given string.

# x = input("enter the string:")
# y = set(x)
# res  = ''.join(y)
# print(res)


# def duplicate_string(x):
#     word = x.split()
#     res = set(word)
#     return ' '.join(res)
# str = input("enter the string:")
# result = duplicate_string(str)
# print(result)    

# def duplicate_string(x): ---------------------> to remove the single worded string
#     result_str = " "
#     prev_char = None
#     for char in x:
#         if char != prev_char:
#             result_str += char
#         prev_char = char
#     return result_str
# input_str = input("enter the string:")
# res = duplicate_string(input_str)
# print(res)            

# def duplicate_string(input_str):------------------------> using the set of string to remove the duplicates
#     words = input_str.split()  
#     result_words = [words[0]]
#     for word in words[1:]:
#         if word != result_words[-1]:
#             result_words.append(word)
#     return ' '.join(result_words)
# input_str = input("Enter the sentence: ")
# result = duplicate_string(input_str)
# print(result)




