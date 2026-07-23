# A function is a named, reusable block of code that performs a specific task. Instead of writing the same code repeatedly, you define it once and "call" it whenever you need it.

# Key parts of a function:

# Name – how you refer to it
# Parameters (optional) – inputs it accepts
# Body – the code that runs
# Return value (optional) – the output it gives back

# In Python:
def greet(name):
    return "Hello, " + name

message = greet("Farah")
print(message)   # Hello, Farah
# =========================================================
# PYTHON STRING FUNCTIONS - COMPLETE REFERENCE
# =========================================================

text = "  Hello World  "

# ---------------------------------------------------------
# 1. len() - returns the number of characters in a string
# ---------------------------------------------------------
print(len("Hello"))          # Output: 5

# ---------------------------------------------------------
# 2. upper() - converts all characters to uppercase
# ---------------------------------------------------------
print("hello".upper())       # Output: HELLO

# ---------------------------------------------------------
# 3. lower() - converts all characters to lowercase
# ---------------------------------------------------------
print("HELLO".lower())       # Output: hello

# ---------------------------------------------------------
# 4. title() - capitalizes the first letter of every word
# ---------------------------------------------------------
print("hello world".title()) # Output: Hello World

# ---------------------------------------------------------
# 5. capitalize() - capitalizes only the first letter of the string
# ---------------------------------------------------------
print("hello world".capitalize())  # Output: Hello world

# ---------------------------------------------------------
# 6. swapcase() - swaps uppercase to lowercase and vice versa
# ---------------------------------------------------------
print("Hello World".swapcase())  # Output: hELLO wORLD

# ---------------------------------------------------------
# 7. strip() - removes spaces from both left and right sides
# ---------------------------------------------------------
print(text.strip())          # Output: "Hello World"

# ---------------------------------------------------------
# 8. lstrip() - removes spaces from the left side only
# ---------------------------------------------------------
print(text.lstrip())         # Output: "Hello World  "

# ---------------------------------------------------------
# 9. rstrip() - removes spaces from the right side only
# ---------------------------------------------------------
print(text.rstrip())         # Output: "  Hello World"

# ---------------------------------------------------------
# 10. find() - returns the index of the first match, -1 if not found
# ---------------------------------------------------------
print("hello world".find("world"))   # Output: 6
print("hello world".find("xyz"))     # Output: -1

# ---------------------------------------------------------
# 11. count() - counts how many times a value appears
# ---------------------------------------------------------
print("hello world".count("o"))      # Output: 2

# ---------------------------------------------------------
# 12. replace() - replaces one substring with another
# ---------------------------------------------------------
print("hello world".replace("world", "python"))  # Output: hello python

# ---------------------------------------------------------
# 13. split() - breaks a string into a list using a separator
# ---------------------------------------------------------
print("a,b,c".split(","))    # Output: ['a', 'b', 'c']

# ---------------------------------------------------------
# 14. join() - joins list items into one string using a separator
# ---------------------------------------------------------
print(",".join(["a", "b", "c"]))     # Output: a,b,c

# ---------------------------------------------------------
# 15. startswith() - checks if string starts with a given value
# ---------------------------------------------------------
print("hello".startswith("he"))      # Output: True

# ---------------------------------------------------------
# 16. endswith() - checks if string ends with a given value
# ---------------------------------------------------------
print("hello".endswith("lo"))        # Output: True

# ---------------------------------------------------------
# 17. isdigit() - checks if all characters are digits
# ---------------------------------------------------------
print("123".isdigit())       # Output: True

# ---------------------------------------------------------
# 18. isalpha() - checks if all characters are letters
# ---------------------------------------------------------
print("hello".isalpha())     # Output: True

# ---------------------------------------------------------
# 19. isalnum() - checks if all characters are letters or numbers
# ---------------------------------------------------------
print("hello123".isalnum())  # Output: True

# ---------------------------------------------------------
# 20. isspace() - checks if the string contains only spaces
# ---------------------------------------------------------
print("   ".isspace())       # Output: True

# ---------------------------------------------------------
# 21. islower() - checks if all letters are lowercase
# ---------------------------------------------------------
print("hello".islower())     # Output: True

# ---------------------------------------------------------
# 22. isupper() - checks if all letters are uppercase
# ---------------------------------------------------------
print("HELLO".isupper())     # Output: True

# ---------------------------------------------------------
# 23. index() - like find(), but gives an error if not found
# ---------------------------------------------------------
print("hello world".index("world"))  # Output: 6

# ---------------------------------------------------------
# 24. in operator - checks if a substring exists inside a string
# ---------------------------------------------------------
print("world" in "hello world")      # Output: True