# ============================================================
# TRUTHY AND FALSY VALUES
# ============================================================
# Falsy values: 0, 0.0, "", [], {}, None, False
# Everything else is considered Truthy
# ============================================================
# QUICK REFERENCE
# ============================================================
# FALSY:                    TRUTHY:
# 0                         5
# 0.0                       -1
# ""                        "Farah"
# None                      "0"  <- careful! this is a string, not the number 0
# False                     True
# ============================================================
# FALSY VALUES - Python treats these as False
# ============================================================

value = 0
if value:
    print("Truthy")
else:
    print("Falsy")      # Output: Falsy (0 is falsy)


value = 0.0
if value:
    print("Truthy")
else:
    print("Falsy")      # Output: Falsy (0.0 is falsy)


value = ""
if value:
    print("Truthy")
else:
    print("Falsy")      # Output: Falsy (empty string is falsy)


value = None
if value:
    print("Truthy")
else:
    print("Falsy")      # Output: Falsy (None is falsy)


value = False
if value:
    print("Truthy")
else:
    print("Falsy")      # Output: Falsy (False is falsy)


# ============================================================
# TRUTHY VALUES - Python treats these as True
# ============================================================

value = 5
if value:
    print("Truthy")      # Output: Truthy (any non-zero number is truthy)
else:
    print("Falsy")


value = -1
if value:
    print("Truthy")      # Output: Truthy (negative numbers are truthy too)
else:
    print("Falsy")


value = "Farah"
if value:
    print("Truthy")      # Output: Truthy (non-empty string is truthy)
else:
    print("Falsy")


value = "0"
if value:
    print("Truthy")      # Output: Truthy (this is a STRING containing "0", not the number 0)
else:
    print("Falsy")


value = True
if value:
    print("Truthy")      # Output: Truthy (True itself is truthy)
else:
    print("Falsy")

# ============================================================
# TERNARY OPERATOR - SIMPLE EXPLANATION
# ============================================================
# The ternary operator is a shortcut way to write a simple if/else
# in just ONE line, instead of writing multiple lines.
# It is mainly used when you just want to assign a value
# based on a condition.


# ============================================================
# NORMAL IF / ELSE (the way you already know)
# ============================================================

age = 20

if age >= 18:
    status = "adult"
else:
    status = "minor"

print(status)
# Output: adult


# ============================================================
# SAME THING WRITTEN AS A TERNARY OPERATOR
# ============================================================
# Syntax:
# variable = value_if_true if condition else value_if_false

age = 20

status = "adult" if age >= 18 else "minor"

print(status)
# Output: adult
# Notice: same result as above, but written in a single line


# ============================================================
# HOW TO READ THE TERNARY LINE
# ============================================================
# status = "adult" if age >= 18 else "minor"
#            |            |             |
#      value if       condition     value if
#        True                        False
#
# Read it like a sentence:
# "status equals 'adult' IF age is >= 18, OTHERWISE status equals 'minor'"


# ============================================================
# ANOTHER SIMPLE EXAMPLE
# ============================================================

number = 7

result = "Even" if number % 2 == 0 else "Odd"

print(result)
# Output: Odd


# Compare it to the normal way of writing the same logic:

number = 7

if number % 2 == 0:
    result = "Even"
else:
    result = "Odd"

print(result)
# Output: Odd
# Same result, just written differently


# ============================================================
# ONE MORE EXAMPLE
# ============================================================

marks = 40

result = "Pass" if marks >= 40 else "Fail"

print(result)
# Output: Pass


# ============================================================
# WHEN TO USE TERNARY OPERATOR
# ============================================================
# Only use it when the if/else is SIMPLE -
# just choosing between two values.
# If the logic becomes long or has many conditions,
# use a normal if/elif/else block instead, since ternary
# can become hard to read if it gets too long.


# ============================================================
# CHAINED COMPARISONS (Python-specific feature)
# ============================================================

age = 25

if 18 <= age <= 60:
    print("Working age")

# Equivalent to: age >= 18 and age <= 60


# ============================================================
# COMMON MISTAKES TO AVOID
# ============================================================

# Mistake 1: Using = instead of ==
# if age = 18:      # SyntaxError! = is assignment, == is comparison

# Correct:
age = 18
if age == 18:
    pass

# Mistake 2: Forgetting the colon
# if age >= 18
#     print("Adult")

# Correct:
if age >= 18:
    print("Adult")

# Mistake 3: Inconsistent indentation (mixing tabs/spaces causes errors)
# if age >= 18:
#   print("Adult")     # 2 spaces
#     print("Vote")      # 4 spaces — IndentationError

# Mistake 4: elif ordering bug
x = 150
if x > 0:
    print("positive")
elif x > 100:          # unreachable — x > 0 already caught it
    print("big")


# ============================================================
# PRACTICE EXERCISE STARTER — Leap Year Checker (#5)
# ============================================================

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")