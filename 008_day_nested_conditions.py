# ============================================================
# NESTED IF STATEMENTS
# ============================================================
#Nested if means putting an if statement inside another if (or elif/else) block. The inner condition only gets checked if the outer condition is already True.
#Think of it like doors inside doors — you can't reach the second door unless you've already opened the first one.
username = "farah"
password = "1234"

if username == "farah": # Python checks username == "farah" first.If False → it skips straight to the outer else → prints "User not found". The inner if is never even looked at.
    if password == "1234": # If True → it goes inside, and now checks password == "1234".
        print("Login successful") # If that's True → prints "Login successful".
    else:
        print("Wrong password") # If that's False → prints "Wrong password".
else:
    print("User not found") # if first condition fails.

# Better practice — combine with 'and' instead of nesting when possible
if username == "farah" and password == "1234":
    print("Login successful")
else:
    print("Login failed")
# example analogy:
if condition_1:              # Level 0
    if condition_2:          # Level 1 (only reached if condition_1 is True)
        if condition_3:      # Level 2 (only reached if condition_1 AND condition_2 are True)
            print("All three conditions are True")
# REAL WOELD EXAMPLE:
year = int(input("Enter a year: "))

if year % 4 == 0:                    # Level 0: divisible by 4?
    if year % 100 == 0:              # Level 1: also divisible by 100?
        if year % 400 == 0:          # Level 2: also divisible by 400?
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")