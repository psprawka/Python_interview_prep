# Test your basic knowledge:


# 1. Define an integer, a float, a string.
# my_int = 6
# my_float = 1.0
# my_str = "Hello!"



# 2. Assign 5 values in one line.
# a, b, c, f, e = 1, 2, 3, 4, 5
# a = b = c = d = e = 0



# 3. Create 4 lists with: only numbers, only strings, only lists and all mixed together.
# list_nb = [1, 4, 14, 5, 8]
# list_str = ["Pola", "Kamis", "Wes"]
# list_list = [["There", "Is", "First", "List"], ["There", "Is", "Second", "One"], ["Third", "One", "Present"]]
# list_all = list_nb + list_str + list_list
# print(list_nb)
# print(list_str)
# print(list_list)
# print(list_all)



# 4. Add, delete, iterate, remove, change, access value in the list.
# my_list = []
# my_list.append("Hello")
# my_list.append(1999)
# my_list.append("It's Polka")
# my_list.append(4)
# print(my_list)
# my_list.remove(1999)
# del my_list[1]
# my_list[0] = "Hi"
# print(my_list)



# 5. Play around with `* - + / % **` on the variables - what is possible for which variable type?
# int1, int2 = 3, 4               #all operations possible
# print(int1 * int2)
# print(int1 + int2)
# print(int1 - int2)
# print(int1 / int2)              #returns float!
# print(int1 % int2)
# print(int1 ** int2)

# str1, str2 = "Hola ", "Pola"    #only '+' possible
# print(str1 + str2)

# list1, list2 = [1, 2], [4, 5]   #only '+' and '*' by integer possible
# print(list1 * 4)
# print(list1 + list2)

# d1, d2 = {1:"Hola", 2:"Pola"}, {3:"Hello", 4:"world"}   #nothing possible on dictionaries

# set1, set2 = set([3, 4]), set([1, 2, 3])
# print(set1 - set2)                                      #only substraction possible               

# tuple1, tuple2 = (1, 2), (3, 4)                         #only '+' and '*' by integer allowed
# print(tuple1 * 2)
# print(tuple1 + tuple2)



# 6. Create two lists containing 10 instances of different variables. You are also required to create a list called big_list, which contains each variable, 10 times each, by concatenating the two lists you have created.



# 7. Write a format string with `%s, %f, %d`.
# format_str = "Hello %s, I guess your age is %d, float for you: %f"
# formated_str = format_str % ("Pola", 20, 1.25)
# formated_str2 = format_str % ("Kamil", 21, 1.75)
# print(formated_str, formated_str2, sep="\n")
    
    

# 8. Test out `index(), count(), [start:stop:step], reverse, startswith(), endswith(), split(), lower(), upper()` functionalities of string.


# 9. Play around with `is not in and or`.


# 10. Create 4 functions with 4 different parameter types: default, keyword, variable numbers and required.


# 11. Create a list with a list inside - does it become one big list or a list with a second list in it?
# mylist = [1, 2, 3, [4.1, 5.1], 6, [7.1, 8.1], 9]
# print(mylist) 
# It becomes a nested list



# 12. Play with exceptions, implement 10 most popular mistakes in python made by the beginners and try/except them all with proper handling.



# 13. Create a class called `Programmer` with attributes `language` and `has_glasses` that inherits from a class called `Person` with `age` and `name` attributes. Implement getters, setters and constructors for them.

# class Person():
#     age = 30
#     name = "John"
    
#     def __init__(self):
#         self.name = "ME"
#         print("Creation of Person done!")
        
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
        
#     def set_name(self, name):
#         self.name = name
#     def set_age(self, age):
#         self.age = age
        
# class Programmer(Person):
#     has_glasses = True
#     language = "C"
    
#     def __init__(self):
#         print("Programmer has been created")
    
#     def get_language(self):
#         return self.language
#     def get_glasses(self):
#         return self.has_glasses
        
#     def set_language(self, lang):
#         self.language = lang
#     def set_glasses(self, glasses):
#         self.has_glasses = glasses
    
# Pola = Programmer()
# Pola.set_age(20)
# print(Pola.get_age(), Pola.get_name())



# 14. Convert the list of weights to numpy array, then all of the weights from kg to lbs. Use the scalar conversion of 2.2 lbs per kg for conversion and print the result array in lbs. `weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]`.


# 15. Fix the code to print out the correct information by changing the string:
#     s = "Hey there! what should this string be?"
#     # Length should be 20
#     print("Length of s = %d" % len(s))
#     # First occurrence of "a" should be at index 8
#     print("The first occurrence of the letter a = %d" % s.index("a"))
#     # Number of a's should be 2
#     print("a occurs %d times" % s.count("a"))
#     # Slicing the string into bits
#     print("The first five characters are '%s'" % s[:5]) # Start to 5
#     print("The next five characters are '%s'" % s[5:10]) # 5 to 10
#     print("The thirteenth character is '%s'" % s[12]) # Just number 12
#     print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
#     print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end
#     # Convert everything to uppercase
#     print("String in uppercase: %s" % s.upper())
#     # Convert everything to lowercase
#     print("String in lowercase: %s" % s.lower())
#     # Check how a string starts
#     if s.startswith("Str"):
#         print("String starts with 'Str'. Good!")
#     # Check how a string ends
#     if s.endswith("ome!"):
#         print("String ends with 'ome!'. Good!")
#     # Split the string into three separate strings,
#     # each containing only a word
#     print("Split the words of the string: %s" % s.split(" "))
    

