# String formatting in Python is how you insert variables/values into a string in a clean, readable way — instead of manually joining strings with +.

# 1. f-strings (modern, preferred way)
# Add an f before the quotes, then put variables inside {}.
name = "Farah"
age = 18

print(f"My name is {name} and I am {age} years old.")
# My name is Farah and I am 18 years old.
# You can even do calculations inside the braces:
print(f"Next year I will be {age + 1}.")
# Next year I will be 19.
# You can put almost any expression inside the braces:
x = 5
y = 3
print(f"Sum: {x + y}")          # Sum: 8
print(f"Squared: {x**2}")       # Squared: 25
print(f"Is x bigger? {x > y}")  # Is x bigger? True
# You can even call functions or methods:(we will learn later)
name = "farah"
print(f"{name.upper()}")   # FARAH
#just make the string in upper case.
# Number formatting:
# You can control decimal places, width, padding, and more using a : inside the braces.
pi = 3.14159265

print(f"{pi:.2f}")     # 3.14   → 2 decimal places
print(f"{pi:.0f}")     # 3      → no decimals
print(f"{1000000:,}")  # 1,000,000 → comma separators
print(f"{7:03}")       # 007    → pad with zeros, width 3
print(f"{7:5}")        # "    7" → pad with spaces, width 5
# Alignment:
word = "hi"
print(f"{word:<10}|")  # "hi        |"  left-align, width 10
print(f"{word:>10}|")  # "        hi|"  right-align
print(f"{word:^10}|")  # "    hi    |"  center-align
# Percentages:
score = 0.856
print(f"{score:.1%}")   # 85.6%
# Debugging shortcut (Python 3.8+):
# Add = after the variable to print both the variable name and its value — handy for debugging:
x = 10
print(f"{x=}")   # x=10
# Nested quotes:
# Since f-strings use {}, you can use different quote types inside without conflict:
name = "Farah"
print(f"Her name is '{name}'")   # Her name is 'Farah'
# Multi-line f-strings:
name = "Farah"
age = 21
message = f"""
Name: {name}
Age: {age}
"""
print(message)

# 2. .format() method
# .format() is the string method used before f-strings became standard (Python 3.6+). It's still widely used, especially in older code, so it's good to know.

print("My name is {} and I am {} years old.".format(name, age))
# You can also use index numbers or names:
print("{0} is {1} years old".format(name, age))
print("{n} is {a} years old".format(n=name, a=age))
# Number formatting with .format():
# Same formatting rules apply as f-strings, just written inside {}:
price = 49.5
print("Price: ${:.2f}".format(price))     # Price: $49.50

num = 7
print("{:03}".format(num))                # 007

pi = 3.14159
print("{:.2f}".format(pi))                # 3.14

# Alignment:
word3 = "hi"
print("{:<10}|".format(word3))   # "hi        |"
print("{:>10}|".format(word3))   # "        hi|"
print("{:^10}|".format(word3))   # "    hi    |"

# Comparison: .format() vs f-strings
name = "Farah"
age = 18

# .format()
print("{} is {} years old".format(name, age))

# f-string (same result, cleaner)
print(f"{name} is {age} years old")
# f-strings are generally preferred now because they're shorter and more readable — .format() is mainly good to recognize when reading other people's code, or if you're working with a Python version older than 3.6.

# 3. % formatting (old style, rarely used now)
print("My name is %s and I am %d years old." % (name, age))
