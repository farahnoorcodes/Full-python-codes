"""
Day 010 - Taking User Input in Python
Covers: input(), typecasting (int, float, bool), split() for multiple values
"""

# ============================================
# Python Input Function - Complete Reference
# ============================================

# In Python, use the input() function to take input from the user:
name = input("Enter your name: ")
print("Hello,", name)

# A few things to keep in mind:
# input() always returns a string — even if the user types a number, you need to convert it:
age = int(input("Enter your age: "))  # use int() function to take integer input from the user
print("age of", name, "is", age)  # this is how you can use inputs to print them

# use float() to take float or decimal input from the user
cgpa = float(input("Enter the cgpa: "))
print("cgpa of", name, "is", cgpa)

# Boolean input example with typecasting
# (typecasting means changing the data type -> e.g changing integer into float, changing numbers into string, etc)

is_student = input("Are you a student? (True/False): ")# it is case sensitive so write True and False  in camel case just like this: True,False
# Example input: True   -> is_student = "True" (this is still a string right now)

is_student = (is_student == "True")  # typecasting happens here
# Typecasting: comparing the string with "True" converts it into an actual bool value

print(is_student)        # Output: True
print(type(is_student))  # Output: <class 'bool'>

# For multiple inputs on one line, split the string using the split() function:
a, b = input("Enter two numbers: ").split()  # use space between numbers to work properly in this function
a, b = int(a), int(b)
print("the sum of these two numbers is =", a + b)

# You can get different types of input from user like: string, float, boolean, integer using split() in a line
# Note: using new variable names here (name2, age2...) so we don't overwrite name/age from earlier
name2, age2, height2, is_active2 = input("Enter string, int, float, bool: ").split()

age2 = int(age2)
height2 = float(height2)
is_active2 = (is_active2 == "True")

print(name2, age2, height2, is_active2)

# split() gives you a fixed number of pieces, so the number of variables on the left
# must match exactly how many words you type, or Python throws a ValueError.
# Example: if you type only 3 words but expect 4 variables, you'll get:
# ValueError: not enough values to unpack (expected 4, got 3)