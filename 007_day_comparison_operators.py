# ============================================================
# COMPARISON OPERATORS (used in conditions)
# ============================================================
# there are some operators in python that is used in conditional statement.
# they are given below:
# 1. == means --> Equals to | example  x == 5
# 2. != means --> not Equals to | example  x != 5
# 3. >  means --> Greater than | example  x > 5
# 4. <  means --> less than | example  x < 5
# 5. <= means --> less than  or Equal to | example  x <= 5
# 6. >= means --> Greater than or Equal to | example  x >= 5
x = 10
print(x == 10)   # True
print(x != 5)    # True
print(x > 5)     # True
# ============================================================
# LOGICAL OPERATORS (combine conditions)
# ============================================================
# and   -> True if BOTH conditions are True
# or    -> True if AT LEAST ONE condition is True
# not   -> Reverses the condition (True becomes False, and vice versa)

age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")

temperature = 40
if temperature > 35 or temperature < 0:
    print("Extreme weather warning")

is_raining = False
if not is_raining:
    print("No umbrella needed")