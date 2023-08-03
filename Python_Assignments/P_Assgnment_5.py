# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

# def Divisible_Multiple():
#     for num in range(1500,2700):
#         if num % 7 == 0 and num % 5 == 0:
#             print(num, end= " ")
# print(Divisible_Multiple())



# 2. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5

# def Number_continue():
#     for num in range(0,6):
#         if num == 3:
#             continue
#         elif num == 6:
#             continue
#         print(num,end =" ")
# Number_continue()


# 3. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# Buzz

# def replace_string():
    # for num in range(1,51): ---------->(# The range should be 1 to 50 (inclusive), so we use 51 as the upper bound.)
#         if num % 3 == 0 and num % 5 == 0:
#             print("FizzBuzz")
#         elif num % 3 == 0:
#             print("Fizz")
#         elif num % 5 == 0:
#             print("Buzz") 
#         else:
#             print(num)
# replace_string()


# 4. Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with two equal sides.
# Expected Output:
# Input lengths of the triangle sides:                                    
# x: 6                                                                    
# y: 8                                                                    
# z: 12                                                                   
# Scalene triangle 


# def check_triangle(x,y,z):
#     for i in x,y,z:
#         if x == y == z:
#             print("Triangle is equilateral")
#         elif x == y and x != z:
#             print("Triangle is isosceles")
#         else:
#             print("Triangle is scalene")
#         break
# side1  = int(input("enter the input lenght of x sides of triangle:"))
# side2  = int(input("enter the input lenght of y sides of triangle:"))
# side3  = int(input("enter the input lenght of z sides of triangle:"))
# res = check_triangle(side1,side2,side3)
# print(res)

# 5. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish

    
# def sum_average(num):
#     sum = 0
#     avg = 0
#     for num in range(1,1+num,1):
#         if num == 0:
#             return 0
#         sum = sum + num
#     avg = sum/num
#     return sum , avg
# input = int(input("enter the number:"))
# res= sum_average(input)
# print(res)   

# x = input("enter the number:")
# num = x.split()
# for i in range(len(num)):
#     num[i] = int(num[i])
# sum =sum(num)
# avg = sum/len(num)
# print("the sum of numbers:",sum)
# print("the average of numbers:",avg)


# 6. Write a Python program to construct the following pattern, using a nested loop number.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

# n = int(input("enter the number of rows:"))
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(i, end = '')
#     print()
        

# 7. Write a Python program that counts the number of elements within a list that are greater than 30.

# def number_count(x):
#     count = 0
#     for i in x:
#         if  int(i) > 30 :
#             count += 1
#     return count
# input = input("enter the number:")
# number_list = input.split()
# print(number_count(number_list))


# 8. Take values of length and breadth of a rectangle from user and check if it is square or not.


# length = int(input("enter the lenght:"))
# breadth = int(input("enter the breadth:"))
# if length == breadth :
#     print("It is a Square")
# else:
#     print("It is a Rectangle")

# 9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.


# def Total_Cost(quantity, unitcost):
#     Total_Cost = quantity * unitcost
    
#     if Total_Cost > 1000 :
#         discount = 0.1 * Total_Cost
#         Total_Cost -= discount
#     return Total_Cost
    
# quantity = int(input("enter the quantity:"))
# unitcost = int(input("enter the unit cost:"))
# res = Total_Cost(quantity,unitcost)
# print(res)


# 10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.


# def net_bonus(salary,year):
#     bonus  = 0.05
#     totalbonus = bonus*salary
#     if year > 5 :
#         salary = salary + totalbonus
#     return totalbonus
# salary = int(input("enter the salary:"))
# year = int(input("enter the year of service:"))
# res = net_bonus(salary,year)
# print(res)
    


# 11. A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

# def Grade_System(grade):
#     for i in grade:
#         if i < 25:
#             print("F")
#         elif i >= 25 and i < 45:
#             print("E")
#         elif i >= 45 and i < 50:
#             print("D")
#         elif i >= 50 and i < 60:
#             print("C")
#         elif i >= 60 and i < 80:
#             print("B")
#         elif i >= 80 and i <=100:
#             print("A")
#         elif i > 100:
#             return "Marks exceeds above 100 which is not proper"
#         break
# input_str = int(input("enter the marks:"))
# res = [input_str]-------------------------------------->because we are  inserting single input integer if not int error occurs
# res1 = Grade_System(res)
# print(res1)


# 12. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.


# x = int(input("enter the number of classes held:"))
# y = int(input("enter the no.of classes attended:"))
# p = (y / x)*100
# if p >= 75 :
#     print("student is allowed to the exam")
# else:
#     print("student is not allowed to the exam")
# print(p)
    
# 13. Take 10 integers from keyboard using loop and print their average value on the screen.

# def keyboard_loop(n):
#     num_list = [int(num) for num in n.split()]
#     res = sum(num_list )
#     avg = res/len(num_list)
#     return avg
# input_int = input("enter the integer:")
# print(keyboard_loop(input_int))

# 14. Print multiplication table of 24, 50 and 29 using loop.

# def multiplication_table(n):
#     print(f'Multiplication Table of : {n}')
#     for i in range(1,11):
#         res = n * i
#         print(f'{n} * {i} = {res}')
# numbers = [24,50,29]
# for num in numbers:
#     print(multiplication_table(num))
#     print()       ----------------------------------.# Add a newline for clarity between different tables     
        

# 15. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). 
# Print average and product of all numbers.


# def average_product():
#     numbers = []
#     while True:
#         user_input = input("Enter an integer or enter 'q' to quit:")
#         if user_input.lower() == 'q':
#             break
#         try:
#             numbers.append(int(user_input))
#         except ValueError:
#             print("Invalid input, Please enter a valid integer or 'q' to quit.")
#     if not numbers:
#         print("No numbers entered.")
#     else:
#         average = sum(numbers) / len(numbers)
#         product = 1
#         for num in numbers:
#             product *= num
#         print("Average:", average)
#         print("Product:", product)
# print(average_product())

# 16. Take inputs from user to make a list. 
# Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.

# def main():
#     input_list = []
#     while True:
#         user_input = input("Enter an element or enter 'done' to stop:")
#         if user_input.lower() == 'done':
#             break
#         input_list.append(user_input)
#     if not input_list:
#         print("The list is empty.")
#         return
#     print("Your list:", input_list)
#     delete_ele = input("Enter the element you want to delete: ")
#     if delete_ele in input_list:
#         input_list.remove(delete_ele)
#         print(f"'{delete_ele}' has been deleted from the list.")
#     else:
#         print(f"'{delete_ele}' not found in the list.")
#     print("Updated list:", input_list)
# main()


# 17. Using range(1,101), make three list, 
# one containing all even numbers
# one containing all odd numbers 
# One containing only prime numbers..

# even_num =[]
# odd_num =[]
# prime_num =[]
# for i in range(1,101):
#     if i % 2 == 0:
#         even_num.append(i)
#     elif i % 2 == 1:
#         odd_num.append(i)
#     for j in range(2,i):
#         if i % j == 0 :
#             break
#     else:
#         prime_num.append(i)
# print("even numbers are:",even_num)
# print("odd numbers are:",odd_num)
# print("prime numbers are:",prime_num)


# 18. From the two list obtained in previous question, make new lists, 
# containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.

# even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 
#                 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
# odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 
#                53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
# num_list = [4, 6, 8, 10, 3, 5, 7, 9]

# divisible_by_4 = [num for num in even_numbers if num % 4 == 0]
# divisible_by_6 = [num for num in even_numbers if num % 6 == 0]
# divisible_by_8 = [num for num in even_numbers if num % 8 == 0]
# divisible_by_10 = [num for num in even_numbers if num % 10 == 0]
# divisible_by_3 = [num for num in odd_numbers if num % 3 == 0]
# divisible_by_5 = [num for num in odd_numbers if num % 5 == 0]
# divisible_by_7 = [num for num in odd_numbers if num % 7 == 0]
# divisible_by_9 = [num for num in odd_numbers if num % 9 == 0]

# print("Numbers divisible by 4:", divisible_by_4)
# print("Numbers divisible by 6:", divisible_by_6)
# print("Numbers divisible by 8:", divisible_by_8)
# print("Numbers divisible by 10:", divisible_by_10)
# print("Numbers divisible by 3:", divisible_by_3)
# print("Numbers divisible by 5:", divisible_by_5)
# print("Numbers divisible by 7:", divisible_by_7)
# print("Numbers divisible by 9:", divisible_by_9)



# 19. From a list containing ints, strings and floats, make three lists to store them separately


# list = [12,"apple","banana","orange",14,17,15.00,78.00,34.67]
# list_int = []
# list_strings =[]
# list_floats =[]
# for i in list:
#     if type(i) == int:
#         list_int.append(i)
#     elif type(i) == str:
#         list_strings.append(i)
#     elif type(i) == float:
#         list_floats.append(i)
# print("the list of integers are:",list_int)
# print("the list of strings are:",list_strings)        
# print("the list of floats are:",list_floats)


# 20.You are given with a list of integer elements. Make a new list which will store square of elements of previous list.


# def integer_element(x):
#     new_list = []
#     for i in x:
#         new_list.append(i*i)
#     print("the new list is:",new_list)   
# input = [20,50,5,6]
# res = integer_element(input)
# print(res)


