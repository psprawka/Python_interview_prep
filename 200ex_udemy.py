# 1. Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("%s, you will turn 100 years old in %d" % (name, 2019 + 100 - int(age)))



# 2. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5 
# Expected Result : 615

# n = input("Enter a number: ")
# nn = int(n + n)
# nnn = int(n + n + n)
# print((int(n)+nn+nnn))



# 3. Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1 
# j = 0,1, n-1.
# Input
# Input number of rows: 3
# Input number of columns: 4  
# Output
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]] 

# i = int(input("Input number of rows: "))
# j = int(input("Input number of columns: "))
# my_list = [[col*row for col in range(j)] for row in range(i)]
# print(my_list)



# 4. Write a Python program to check a triangle is valid or not 

# def if_valid_triangle(a, b, c):
#     print("Sides: %d, %d, %d - " % (a, b, c), end = "")
#     if a + b > c and a + c > b and b + c > a:
#         print("Triangle is valid.")
#     else:
#         print("Triangle is not valid.")
        
# if_valid_triangle(1, 2, 3)
# if_valid_triangle(7, 10, 5)
# if_valid_triangle(1, 10, 12)
# if_valid_triangle(3, 5, 8)
# if_valid_triangle(11, 1, 3)
# if_valid_triangle(4, 9, 6)



# 5. Write a Python program to construct the following pattern, using a nested loop number.
# 1
# 22
# 333 
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

# for i in range(1, 10):
#     for j in range(i):
#         print(i, end="")
#     print()



# 6. Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# n = 5
# for i in range(1, n):
#     print("*" * i)
# for i in range(n, 0, -1):
#     print("*" * i)



# 7. Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6 
# Digits 2

# input = input("Insert a string: ")
# digits, letters = 0, 0
# for char in input:
#     if char.isdigit():
#         digits += 1
#     elif char.isalpha():
#         letters += 1
# print("digits: %d | letters: %d" % (digits, letters))



# 8. Count the number of even and odd numbers from a series of numbers
# Input 
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# Output
# Number of even numbers : 4
# Number of odd numbers : 5 

# def even_odd(tup):
#     even = sum(not x % 2 for x in tup)
#     odd = sum(x % 2 for x in tup)
#     print("Tuple: %s | Even: %d | Odd: %d" % (tup, even, odd))
# even_odd((2, 4, 5, 6, 7, 7, 7, 7, 7))
# even_odd((1, 1, 1, 1, 1, 1, 1, 1, 1))



# 9. Write a Python program to get the Fibonacci series between 0 to 50

# def fib(size):
#     a, b = 0, 1
#     for i in range(size):
#         if i == 0 or i == 1:
#             yield i
#         c = a + b
#         a, b = b, c
#         yield c

# my_gen = fib(50)
# for i in my_gen:                    #for i in fib(50):
#     print("%d, " % i, end="")



# 10. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700

# my_list = [x for x in range(1500, 2700) if x % 7 == 0 and not x % 5]
# print(my_list)



# 11. Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

# import random as rd
# rand = rd.randint(1, 9)
# number = 0
# while number is not rand:
#     number = int(input("Guess the number: "))
#     if number > rand:
#         print("Your number is too high.")
#     else:
#         print("Your number is too low.")
# print("You guessed right!")



# 12. Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
# Input
# W3r@100a
# Output
# Valid password

# password = input("Enter new password: ")
# upper, lower, digit, char, len = 0, 0, 0, 0, 0
# for c in password:
#     if c.isupper():
#         upper += 1
#     elif c.islower():
#         lower += 1
#     elif c.isdigit():
#         digit += 1
#     elif c == '$' or c == '#' or c == '@':
#         char += 1
#     len += 1
# if not upper or not lower or not char or not digit or len > 16 or len < 6:
#     print("Password is invalid, sucker.")
# else:
#     print("Password is valid.")
    


# 13. Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.

# def which_triangle(a, b, c):
#     if a == b == c:
#         print("An equilateral triangle!")
#     elif a != b and b != c and c != a:
#         print("A scalene triangle!")
#     else a == b or a == c or b == c:
#         print("An isosceles triangle!")

# which_triangle(1, 1, 1)
# which_triangle(1, 2, 0)
# which_triangle(2, 4, 3)
# which_triangle(1, 3, 1)



# 14. Write a Python program to check whether an alphabet is a vowel or consonant.

# vowels = "aeiouAEIOU"
# input = input("Enter a character: ")
# for x in input:
#     print("vowel") if x in vowels else print("consonant")



# 15. Convert a list of characters into a string
# Input ['a', 'b', 'c', 'd']
# Output abcd

# my_list = ['a', 'b', 'c', 'd']
# string = ''.join(my_list)   # -> if mixed elements: [str(x) for x in my_list])
# print(string)



# 16. Write a Python program to check whether a list contains a sublist.
# Input
# a = [2,4,3,5,7]
# b = [4,3]
# c = [3,7]

# def is_sublist(list_a, pattern):
#     my_list = [x for x in range(0, len(list_a)) if list_a[x:x+len(pattern)] == pattern]
#     return True if my_list else False

# a = [2,4,3,5,7]
# b = [4,3]
# c = [3,7]
# print(is_sublist(a, c))
# print(is_sublist(a, b))



# 17. Write a Python program to find common items from two lists.
# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# {'Green', 'White'}

# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# set1 = set(color1)
# set2 = set(color2)
# print(set1.intersection(set2))
# print(set1 & set2)



# 18. Write a Python program to get the difference between the two lists
# Input 
# list1 = [1, 2, 3, 4]
# list2 = [1, 2]
# Output
# [3,4]

# list1 = [1, 2, 3, 4]
# list2 = [1, 2, 5]
# set1 = set(list1)
# set2 = set(list2)
# print(list(set1.symmetric_difference(set2)))
# print(list(set1 ^ set2))



# 19. Write a Python program to get the maximum number from a list.
# max_num_in_list([1, 2, -8, 0])
# return 2

# def max_num_in_list(list_x):
#     return (max(list_x))

# list1 = [1, 2, -8, 0]
# print(max_num_in_list(list1))



# 20. Write a Python program to get the frequency of the elements in a list.
# input: my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# outout: {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}

# from collections import Counter

# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# print(dict(Counter(my_list)))



# 21. Write a Python program to generate all permutations of a list in Python
# Input [1,2,3]
# Output [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# import itertools

# my_list = [1, 2, 3]
# print(list(itertools.permutations(my_list)))



# 22. Write a Python program to remove duplicates from a list.
# Input a = [10,20,30,20,10,50,60,40,80,50,40]
# Output {40, 10, 80, 50, 20, 60, 30} 

# a = [10,20,30,20,10,50,60,40,80,50,40]
# print(set(a))



# 23. Write a Python program to find the second smallest number in a list.
# input
# second_smallest([1, 2, -8, -2, 0])
# output
# -2

# def second_smallest(my_list):
#     second = smallest = float('inf')
#     for x in my_list:
#         if x < smallest:
#             second, smallest = smallest, x
#         elif x < second:
#             second = x
#     return second

# print(second_smallest([1, 2, -8, -2, 0]))
# print (second_smallest([1, 2, -8, -2, 0, 1, 10, -9]))
# print (second_smallest([-11, -9]))
# print (second_smallest([]))



# 24. # Write a Python program to sum all the items in a list
# Example sum_list([1,2,-8])
# Return -5

# numbers = [1, 3, -7]
# print(sum(numbers))



# 25. Write a Python program to create a Caesar encryption
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
# The method is named after Julius Caesar, who used it in his private correspondence.
# plaintext:  defend the east wall of the castle
# ciphertext: efgfoe uif fbtu xbmm pg uif dbtumf

# def caesar_encrypt(s, shift):
#     ret = ""
#     for i in range(len(s)):
#         if 'A' <= s[i] <= 'Z':
#             ret += chr((ord(s[i]) + shift - 65) % 27 + 65)
#         elif 'a' <= s[i] <= 'z':
#             ret += chr((ord(s[i]) + shift - 97) % 27 + 97)
#         else:
#             ret += s[i]
#     return ret

# print(caesar_encrypt("defend the east wall of the castle", 1))



# 26. Write a Python program to change a given string to a new string where the first and last chars have been exchanged 

# input = input("Enter a string: ")
# new_str = input[-1:] + input[1:-1] + input[:1]
# print(new_str)



# 27. Write a Python program to count the number of characters (character frequency) in a string.
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

# from collections import Counter

# str1 = "google"
# elements = Counter(str1)
# print(dict(elements))



# 28. Write a Python function to create the HTML string with tags around the word(s).
# Sample function and result : 
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

# def add_tags(tag, text):
#     tag_s = "<" + tag + ">"
#     tag_e = "</" + tag + ">"
#     return tag_s + text + tag_e

# def add_tags2(tag, text):
#     return "<%s>%s</%s>" % (tag, text, tag)
    
# print(add_tags('i', 'Python'))
# print(add_tags('b', 'Python Tutorial'))
# print(add_tags2('i', 'Python'))
# print(add_tags2('b', 'Python Tutorial'))



# 29. Write a Python function that takes a list of words and returns the length of the longest one.

# list1 = ["Hello world", "Hi", "Hello", "Hey", "Hello everyone"]
# print("Max: " + max(list1, key=len))
# print("Min: " + min(list1, key=len))



# 30. Write a Python program to remove the nth index character from a nonempty string.

# def remove_idx(str1, n):
#     return str1[:n] + str1[n+1:]

# input = input("Enter a string: ")
# print(remove_idx(input, 2))



# 31. 'The quick brown fox jumps over the lazy dog.'
# input : "The quick brown fox jumps over the lazy dog."
# output : "dog. lazy the over jumps fox brown quick The "

# import re

# str1 = "The quick brown fox jumps over the lazy dog."
# str2 = " "
# words = re.split(' |\n|\t|,', str1)
# print(str1 + "\n" + str2.join(words[::-1]))



# 32. Write a Python program to calculate the length of a string.

# def my_len(str1):
#     len = 0
#     for i in str1:
#         len += 1
#     return len

# print(my_len("Hello!0"))



# 33. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white

# import re

# input = input("Enter a sequence of words separated by comma: ")
# words = sorted(set(re.split(", |,", input)))
# print(words)



# 34. Write a Python program to count the occurrences of each word in a given sentence.

# from collections import Counter

# inp = input("Enter a string: ")
# words = Counter(inp.split())
# print(dict(words))

# input = input("Enter a string: ")
# words = input.split()
# count = {}
# for word in words:
#     if word in count:
#         count[word] += 1
#     else:
#         count[word] = 1
# print(count)



# 35. Check if a given key already exists in a dictionary
# input
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# is_key_present(5)
# is_key_present(9)
# output
# Key is present in the dictionary                                                                           
# Key is not present in the dictionary

# def is_key_present(dictionary, key):
#     if key in dictionary:
#         print("Key is present in the dictionary.")
#     else:
#         print("Key is not present in the dictionary.")

# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# is_key_present(d, 5)
# is_key_present(d, 9)
# is_key_present(d, "cat")



# 36. Write a Python script to concatenate following dictionaries to create a new one.
# Input
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Output
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50, 6:60}

# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)



# 37. Write a Python program to iterate over dictionaries using for loops.

# d = {"color":"pink", "year":1999, "name":"Polcia", "model":True}
# for key, value in d.items():
#     print("key - value:\t%s - %s" % (key, value))
# for x in d:
#     print("x = %s\td[x] = %s" % (x, d[x]))



# 38. Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary :  {0: 0, 1: 2, 2: 1, 3: 4, 4: 3}                                                      
# Dictionary in ascending order by value :  [(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)]                         
# Dictionary in descending order by value :  [(4, 3), (3, 4), (2, 1), (1, 2), (0, 0)]

# d = {0: 0, 1: 2, 2: 1, 3: 4, 4: 3} 
# d_list = []
# for key, value in d.items():
#     tup = (key, value)
#     d_list.append(tup)
# print(sorted(d_list))
# print(sorted(d_list, reverse=True))
# print(sorted(d.items()))
# print(sorted(d.items(), reverse=True))



# 39. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.

# d = {x:x**2 for x in range(1, 16)}
# print(d)



# 40. Sum all the items in a dictionary
# Input {'data1':100,'data2':-54,'data3':247}
# Output 293

# d = {'data1':100, 'data2':-54, 'data3':247}
# print(sum(d.values()))



# 41. Write a Python program to get the file size of a plain file.
# Use test.txt file at same folder

# import os

# statinfo = os.stat("test.txt")
# print(statinfo.st_size)



# 42. Write a Python program to read first n lines of a file.
# Use test.txt file

# def read_n_lines(fname, n):
#     with open(fname) as f:
#         for i in range(n):
#             print(f.readline().strip())

# from itertools import islice

# def read_n_lines2(fname, n):
#     with open(fname) as f:
#         for line in islice(f, n):
#             print(line.strip())
            
# read_n_lines("test.txt", 2)
# read_n_lines2("test.txt", 2)



# 43. Write a python program to find the longest words in a file.
# Use test.txt file in same folder

# def longest_in_file(fname):
#     with open(fname) as f:
#         words = f.read().split()
#         max_len = len(max(words, key=len))
#         words_max = [x for x in words if len(x) == max_len]
#         print(words_max)
        
# longest_in_file("test.txt")



# 44. Write a Python program to read a random line from a file.
# Using test.txt

# import random

# def read_random(fname):
#     with open(fname) as f:
#         lines = f.readlines()
#         print(random.choice(lines).strip())
        
# read_random("test.txt")



# 45. (!) Write a Python program to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
# These brackets must be close in the correct order, 
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{‌{‌{" are invalid.



# 46. Write a Python class named Circle constructed by a radius and two methods which
# will compute the area and the perimeter of a circle.

# import math

# class Circle:
#     def __init__(self, r):
#         self.radius = r
    
#     def compute_area(self):
#         return math.pi * self.radius ** 2
        
#     def compute_perimeter(self):
#         return 2 * math.pi * self.radius
        
# c1 = Circle(5)
# print(c1.compute_area())
# print(c1.compute_perimeter())



# 47. Write a Python class to convert a roman numeral to an integer
# Sample input
# 'MMMCMLXXXVI'
# 'MMMM'
# 'C'
# Sample output
# 3986                                                                                                          
# 4000                                                                                                          
# 100

# class RomanToInt:
#     d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    
#     def __init__(self, r):
#         self.roman = r
#         self.roman_len = len(r)
#         self.result = 0
        
#     def romanToInt(self):
#         for i in range(self.roman_len):
#             if i == self.roman_len-1 or self.d[self.roman[i]] >= self.d[self.roman[i + 1]]:
#                 self.result += self.d[self.roman[i]]
#             else:
#                 self.result -= self.d[self.roman[i]]
    
#     def printResult(self):
#         print(self.result)
        
# inp = input("Enter roman numeral here: ")
# r1 = RomanToInt(inp)
# r1.romanToInt()
# r1.printResult()



# 48. Write a Python program to convert an integer to a roman numeral.
# Input 1, 4000
# Output I, MMMM

# from collections import OrderedDict
# 
# d = OrderedDict({"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC": 90, "L": 50, \
                    # "XL": 40, "X":10, "IX": 9, "V":5, "IV":4, "I":1})     
# inp = int(input("Enter integer for roman: "))
# roman = ""
# for key, val in d.items():
#     count = int(inp / val)
#     roman += key * count
#     inp -= val * count
# print(roman)



# 49. Write a Python class which has two methods: getString and printString. 
# getString accepts a string from the user and printString prints the string in upper case.

# class UserString:
#     def __init__(self):
#         pass
#     def getString(self):
#         self.string = input("Enter a string: ")
#     def printString(self):
#         print(self.string.upper())
        
# str1 = UserString()
# str1.getString()
# str1.printString()



# 50. Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle. 

# class Rect:
#     def __init__(self, l, w):
#         self.len = l
#         self.wid = w
#     def computeArea(self):
#         return self.len * self.wid

# rectangle = Rect(3, 12)
# print(rectangle.computeArea())



# 51. Write a Python class to reverse a string word by word.
# Input "hello world"
# Output "world hello"

# class ReverseStr:
#     def rev_words(self, inp):
#         return " ".join(inp.split()[::-1])
        
# inp = input("Enter a str: ")
# s1 = ReverseStr()
# print(s1.rev_words(inp))



# 52. Write a Python program to find the three elements that sum to zero from a set (array) of n real numbers.
# Input: [-25, -10, -7, -3, 2, 4, 8, 10]
# Output: [[-10, 2, 8], [-7, -3, 10]] 

# from operator import itemgetter

# def find_three(nums, n):
#     list_results = []
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             for k in range(len(nums)):
#                 if j != k != i and nums[i] + nums[j] + nums[k] == 0:
#                     new = sorted([nums[i], nums[j], nums[k]])
#                     if new not in list_results:
#                         list_results.append(new)
#     return list_results

# numbers = [-25, -10, -7, -3, 2, 4, 8, 10]
# numbers.sort()
# print(find_three(numbers, 0))



# 53. Write a Python program to convert a binary number to decimal number. 

# def bin_to_dec(n):
#     power = sum = 0
#     for x in n[::-1]:
#         if int(x):
#             sum += 2**power
#         power += 1
#     return sum
        
# print(bin_to_dec("10010100010101001"))



# 54. Write a Python program to flip a coin 1000 times and count heads and tails. 

# import random as rd

# res = [0, 0]
# for _ in range(1000):
#     res[rd.randint(0, 1)] += 1
# print("Heads: %s, Tails: %s" % (res[0], res[1]))



# 55. Write a Python program to generate a series of unique random numbers.

# import random as rd

# def n_unique(n, max_range):
#     print(rd.sample(range(max_range), n))
    
# n_unique(10, 10000)



# 56. Write a Python function to round up a number to specified digits.         

# import math

# def round_up(x, digits):
#     multiply = 10 ** digits
#     return (math.ceil(x * multiply) / multiply)

# x = 123.01247
# print(round_up(x, 0))
# print(round_up(x, 1))
# print(round_up(x, 2))
# print(round_up(x, 3))



# 57. Write a Python program to calculate the standard deviation of the following data.
# Input
# Sample Data:  [4, 2, 5, 8, 6]                                                                                 
# Output
# Standard Deviation :  2.23606797749979

# import statistics as stat
# list1 = [4, 2, 5, 8, 6]
# print(stat.stdev(list1))



# 58. Write a Python program to convert Year/Month/Day to Day of Year.

# import time
# time_struct = time.strptime("19 Nov 21", "%y %b %d")
# print (time_struct.tm_yday)



# 59. Write a Python program to get the current time in Python. 

# import datetime
# import time

# print(datetime.datetime.now()) 
# print(time.ctime())
# print(time.asctime(time.localtime(time.time())))



# 60. Write a Python script to display the various Date Time formats.
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week

# import time
# import calendar

# y, m, d, h, m, s, wd, yd, isd = time.localtime(time.time())
# print("Current date and time:", time.ctime())
# print("Current year:", y)
# print("Month of year:", m)
# print("Week number of the year:", int(yd / 7))
# print("Weekday of the week:", calendar.day_name[wd])
# print("Day of year:", yd)
# print("Day of the month:", d)
# print("Day of week:", wd + 1)



# 61. Write a Python program to get current time in milliseconds in Python.

# import time
# print(int(time.time() * 1000))



# 62. Write a Python program to subtract five days from current date

# import datetime as dt
# print(dt.datetime.today() - dt.timedelta(days=5))



# 63. Write a Python program to find all five characters long word in a string.
# Input: 'The quick brown fox jumps over the lazy dog.'
# Output: ['quick', 'brown', 'jumps']

# n = 5
# str1 = 'The quick brown fox jumps over the lazy dog.'
# print ([x for x in str1.split() if len(x) == n])



# 64. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
# Input
# "ABCDEFabcdef123450"
# "*&%@#!}{"
# Output
# True                       
# False

# def if_only(str1):
#     x = [x for x in str1 if not x.isdigit() and not x.isalpha()]
#     return False if len(x) else True

# s1 = "ABCDEFabcdef123450"
# s2 = "*&%@#!}{"
# print(s1, "->", if_only(s1))
# print(s2, "->", if_only(s2))



# 65. Write a Python program to find the occurrence and position of the substrings within a string.
# Input
# text = 'Python exercises, PHP exercises, C# exercises'
# pattern = 'exercises'
# Output
# Found "exercises" at 7:16                                                                                     
# Found "exercises" at 22:31                                                                                    
# Found "exercises" at 36:45

# import re

# text = 'Python exercises, PHP exercises, C# exercises - exexercises'
# pattern = 'exercises'
# for item in re.finditer(pattern, text):
#     print("Found \"", pattern, "\" at ", item.start(), ":", item.end(), sep="")
#     print("Found \"%s\" at %d:%d" % (pattern, item.start(), item.end()))



# 66. Write a Python program to remove everything except alphanumeric characters from a string.
# Input
# '**//Python Exercises// - 12. '
# Output
# PythonExercises12

# text = '**//Python Exercises// - 12. '
# print("".join([x for x in text if x.isalpha() or x.isdigit()]))



# 67. Write a Python program to remove the parenthesis area in a string.
# Input: ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
# Output: ["example", "w3resource", "github", "stackoverflow"]

# def remove_areas(items):
#     list_items = []
#     for string in items:
#         left = string.find('(')
#         right = string.find(')')
#         list_items.append(string[:left] + string[right+1:])
#     return list_items

# l = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
# print(remove_areas(l))


# 68. Remove all whitespaces from a string.
# Input: ' Python    Exercises '
# Output: PythonExercises

# import re
# text = ' Python    Exercises '
# print("".join(text.split()))



# 69. #Write a Python program to remove leading zeros from an IP address.
# Input
# "216.08.094.196"
# Output
# 216.8.94.196

# ip = "216.08.094.196"
# ip_list = ip.split(".")
# ip_list_int = list(map(int, ip_list))
# print(".".join(map(str, ip_list_int)))



# 70. Find the length of longest non-repeatable substring in a string
# I'm going to use sliding window pattern - with the help of start and 
#   end variables, I'm going to go through a string char by char. For 
#   each character, I check if I already have it in my queue of visited
#   characters. If no, go further. If yes, update start index.
#   Time complexity: O(n); Space complexity: O(n)

# from collections import deque

# s, e, max_len = 0, 0, 0
# str1 = "abcdxyz"
# queue = deque() 

# while (e < len(str1)):
#     queue.append(str1[e])
#     while queue.count(str1[e]) > 1:
#         queue.popleft()
#         s += 1
#     if e - s + 1 > max_len:
#         max_len = e - s + 1
#     e += 1
# print("Max len of longest substring:", max_len)



# 71. Given a collection of intervals which are already sorted by start number, merge all overlapping intervals.
# For example,
# Given [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]],
# return [[1, 10], [11, 18], [19, 22]]

# def merge_intervals(items):
#     int_len = len(intervals)
#     if int_len < 2:
#         return items
#     overlaps = []
#     start = end = float("inf")
#     for i in range(int_len):
#         if start == end == float("inf"):
#              start, end = items[i]
#         if i+1 < int_len and items[i][1] >= items[i+1][0]:
#             end = items[i+1][1]
#         else:
#             overlaps.append([start, end])
#             start = end = float("inf")
#     return overlaps
    
# def merge_intervals(items):
#     for i in range(len(items)):
#         while i < len(items)-1 and items[i][1] >= items[i+1][0]:
#             items[i][1] = items[i+1][1]
#             del items[i+1]
#     return items
    
# org_intervals = [[1,3], [2,5]]
# print(merge_intervals(org_intervals))



# 72. Consider an array of non negative integers. 
# A second array is formed by shuffling the elements of the first array and deleting a random element.
# Given these two arrays, find which one is missing in the second array.
# Input: [1, 2, 3, 4, 5, 5, 6, 7] [3, 7, 2, 1, 4, 6, 5]
# Output: 5 is the missing number

# def find_missing(org_list, del_list): # for many missing
#     shared_dict = {}
#     for item in org_list:
#         shared_dict[item] = shared_dict.get(item, 0) + 1
#     for item in del_list:
#         if shared_dict.get(item) == 1:
#             del shared_dict[item]
#         else:
#             shared_dict[item] -= 1
#     return list(shared_dict.keys())

# def find_missing2(org_list, del_list): # for one missing
#     return sum(org_list) - sum(del_list)

# list1 = [1, 2, 3, 4, 5, 5, 6, 7]
# list2 = [3, 7, 2, 1, 4, 6, 5]
    
# print(find_missing2(list1, list2))
# print(find_missing(list1, list2))



# 73. Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3,
# the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
# Note:
# Try to come up as many solutions as you can,
# there are at least 3 different ways to solve this problem.
 
# def rotate_array(array, k):
#     print(array[-k:] + array[: len(array) - k])
    
# rotate_array([1, 2, 3, 4, 5, 6, 7], 3)



# 74. Given a sorted integer array without duplicates,
# return the summary of its ranges.
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

# def sum_ranges(nums):
    # ranges = []
#     i = 0
#     while i < len(nums):
#         s = i
#         while i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:
#             i += 1
#         if (s == i)
#             ranges.append(str[nums[i])
#         else:
#             ranges.append(str(nums[s]) + "->" + str(nums[i]))
#         i += 1
#     return ranges

# nums = [0,1,2,4,5,7,8,9,13]
# print(sum_ranges(nums))
    
    
    
# 75. Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution
# Example:
#     Given nums = [2, 7, 11, 15], target = 26,
#     Because nums[2] + nums[3] = 11 + 15 = 26,
#     return [2, 3].

# def add_two(nums, target):
#     all_nums = {}
#     for i in range(len(nums)):
#         b = all_nums.get(target - nums[i], -1)
#         if b != -1:
#             return [b, i]
#         all_nums[nums[i]] = i
#     return None

# nums = [2, 7, 11, 15]
# print(add_two(nums, 13))



# 76. Write a Python program to sort a list of elements using the bubble sort algorithm.

# def bubble_sort(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums) - 1):
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]

# nums = [6, 4, 2, 3, 1, 5, 3, -6]
# bubble_sort(nums)
# print(nums)



# 77. Write a Python program to sort a list of elements using the insertion sort algorithm.

# def insertion_sort(nums):
#     for i in range(len(nums)):
#         j = i
#         while j > 0 and nums[j] < nums[j-1]:
#             nums[j-1], nums[j] = nums[j], nums[j-1]
#             j -= 1

# nums = [6, 4, 2, 3, 1, 5, 3, -6]
# insertion_sort(nums)
# print(nums)
  


# 78. Write a Python program to sort a list of elements using the selection sort algorithm.

# def selection_sort(nums):
#     for i in range(len(nums)):
#         min = i
#         for j in range(i, len(nums)):
#             if nums[min] > nums[j]:
#                 min = j
#         nums[i], nums[min] = nums[min], nums[i]

# nums = [6, 4, 2, 3, 1, 5, 3, -6]
# selection_sort(nums)
# print(nums)



# 79. (!) Write a Python program to sort a list of elements using shell sort algorithm.
# Note : According to Wikipedia "Shell sort or Shell's method, is an in-place comparison sort. 
# It can be seen as either a generalization of sorting by exchange (bubble sort) or sorting by insertion (insertion sort). 
# The method starts by sorting pairs of elements far apart from each other, then progressively reducing the gap between
# elements to be compared. Starting with far apart elements can move some out-of-place elements into position faster than
# a simple nearest neighbor exchange."



# 80. Write a Python program to sort a list of elements using the merge sort algorithm.

# def merge(arr, start, end, mid):
#     i, j = start, mid
#     arr_temp = []
#     # print("---\ni: %d, mid: %d, j: %d, end: %d" % (i, mid, j, end))
#     # print("arr1:", arr[i:mid], "arr2:", arr[mid:end], "\n---")
#     while i < mid and j < end:
#         if arr[i] > arr[j]:
#             arr_temp.append(arr[j])
#             j += 1
#         else:
#             arr_temp.append(arr[i])
#             i += 1
#     while i < mid:
#         arr_temp.append(arr[i])
#         i += 1
#     while j < end:
#         arr_temp.append(arr[j])
#         j += 1
#     # print(arr_temp)
#     arr = arr_temp
        

# def merge_sort(arr, start, end):
    
#     if (start < end):
#         mid = int((end - start) / 2 + start)
#         print("MERGE_SORT:        start %d, end %d, mid %d" % (start, end, mid))
#         print("MERGE_SORT: arr1:", arr[start:mid], "arr2:", arr[mid:end], "\n")
#         merge_sort(arr, start, mid)
#         merge_sort(arr, mid + 1, end)
#         merge(arr, start, end, mid)


# def merge(arr, start1, m, r): 
#     n1 = m - start1 + 1
#     n2 = r- m 
  
#     L = [0] * (n1) 
#     R = [0] * (n2) 
  
#     for i in range(0 , n1): 
#         L[i] = arr[start1 + i] 
  
#     for j in range(0 , n2): 
#         R[j] = arr[m + 1 + j] 
  
#     i = 0 
#     j = 0
#     k = start1 
#     while i < n1 and j < n2 : 
#         if L[i] <= R[j]: 
#             arr[k] = L[i] 
#             i += 1
#         else: 
#             arr[k] = R[j] 
#             j += 1
#         k += 1
  
#     while i < n1: 
#         arr[k] = L[i] 
#         i += 1
#         k += 1
  
#     while j < n2: 
#         arr[k] = R[j] 
#         j += 1
#         k += 1
  
# # start1 is for left index and r is right index of the 
# # sub-array of arr to be sorted 
# def mergeSort(arr,start,mid): 
#     if start < mid: 
  
#         # Same as (start1+r)/2, but avoids overflow for 
#         # large start1 and h 
#         middle = (start+(mid-1))/2
  
#         # Sort first and second halves 
#         mergeSort(arr, start, middle) 
#         mergeSort(arr, middle+1, mid) 
#         merge(arr, start, middle, r) 





# def merge(arr, start, end, mid):
#     i, j = start, mid
#     arr_temp = []
#     #print("---\ni: %d, mid: %d, j: %d, end: %d" % (i, mid, j, end))
#     print("arr1:", arr[i:mid], "arr2:", arr[mid:end], "\n---")
#     while i < mid and j < end:
#         if arr[i] > arr[j]:
#             arr_temp.append(arr[j])
#             j += 1
#         else:
#             arr_temp.append(arr[i])
#             i += 1
#     while i < mid:
#         arr_temp.append(arr[i])
#         i += 1
#     while j < end:
#         arr_temp.append(arr[j])
#         j += 1
#     print(arr_temp)
#     return arr_temp
        

# def merge_sort(arr):
    
#     if (len(arr) > 1):
#         mid = int(len(arr) / 2)
#         print("MERGE_SORT ARR: ", arr)
#         # print("MERGE_SORT:        start %d, end %d, mid %d" % (0, len(arr), mid))
#         # print("MERGE_SORT: arr1:", arr[:mid], "arr2:", arr[mid:], "\n")
#         merge_sort(arr[:mid])
#         merge_sort(arr[mid:])
#         arr = merge(arr, 0, len(arr), mid)
#         print("ARR: ", arr)
    
# k = [1, 5, 4 , 2, 0, 7]
# merge_sort(k)
# print(k)
    

# def merge_sort(arr, start, end):
#     mid = int((end - start) / 2)
#     merge_sort(arr[:mid])
#     merge_sort(arr[int(arr_len/2):])
#     merge()



# 81.(!) Write a Python program to sort a list of elements using the quick sort algorithm.

# def quicksort(arr):
#     pivot



# 82. Write a Python program for sequential search.
# Sequential Search: In computer science, linear search or sequential search is a method for finding a particular value in a list
# that checks each element in sequence until the desired element is found or the list is exhausted. The list need not be ordered.

# def sequential_search(seq, to_find):
#     for i in range(len(seq)):
#         if seq[i] == to_find:
#             print("Item found")
#             break
#     else:
#         print("Item not found")

# sequential_search(["Pola", "is", 10, ['a', 'b'], "nice"], "nice")
# sequential_search([1, 50, 43, 20, 75, 30, 21], 30)



# 83. Write a Python program for binary search. 
# Binary Search : In computer science, a binary search or half-interval search algorithm finds the position of a target value
# within a sorted array. The binary search algorithm can be classified as a dichotomies divide-and-conquer search algorithm and 
# executes in logarithmic time.

# def binary_search(seq, to_find):
#     s, e = 0, len(seq)
#     while e - s >= 0:
#         i = int((e - s) / 2 + s)
#         if seq[i] == to_find:
#             return seq[i], i
#         if seq[i] > to_find:
#             e = i - 1
#         else:
#             s = i + 1
#     return None

# seq = [1, 10, 15, 16, 23, 42, 43, 46, 50, 51, 54, 55, 56]
# print(binary_search(seq, 54))
# print(binary_search(seq, 10))
# print(binary_search(seq, 5))
# print(binary_search(seq, 42))
# print(binary_search(seq, 1))
# print(binary_search(seq, 56))



# 84. Write a Python program to calculate the value of 'a' to the power 'b'. 

# def power_of(a, b):
#     # return a**b 
#     if a == 0:
#         return 1
#     return (pow(a,b))
# print(power_of(2, 8))

        
        
# 85. Write a program to solve the Fibonacci sequence using recursion. 

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)
# print(fib(4))      


    
# 86. Write a Python program to get the factorial of a non-negative integer.   
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
# print(factorial(4))



# 87. Write a Python program to find the greatest common divisor (gcd) of two integers.

# def gcd(a, b):
#     low, high = min(a,b), max(a,b)
#     if low == 0:
#         return high
#     return gcd(low, high%low)

# print(gcd(60, 48))



# 88. Write a Python program to calculate the sum of a list of numbers. (in recursion fashion)

# def sum_list(my_list, n):
#     if n < 0:
#         return 0
#     return my_list[n] + sum_list(my_list, n-1)
    
# def sum_list2(my_list):
#     if len(my_list) == 1:
#         return my_list[0]
#     return my_list[0] + sum_list2(my_list[1:])
    
# my_list = [1, 5, 8, 3, 4, 0, 7]
# print(sum_list(my_list, len(my_list) - 1))
# print(sum_list2(my_list))





# nums = [1,2,3,4,5,80,5,5,5,5,5,6,7,8,9,10,11,12,13,14]

# for i in nums[:]:
#     print("1. i = %d, len(nums): %d" %(i, len(nums)))
#     if i < 14 and nums[i] == 5:
#         print("2. REMOVING I = %d" % i)
#         del nums[i]
#         i = 1
#     print("3. i = %d, nums = " % i, nums)
    
# for i in nums[:]:
#     print("1. i = %d, len(nums): %d" %(i, len(nums)))
#     print(nums[i])