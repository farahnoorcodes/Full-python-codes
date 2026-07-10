# Conditional statements let your program make decisions and execute different code based on whether something is True or False.
# 1. if condition:
age = 20

if age >= 18:
    print("You are an adult")
# Rules:

# Condition must evaluate to True or False (or something "truthy"/"falsy")
# Colon (:) is required after the condition
# Code inside the block must be indented (4 spaces is convention)
# 2. if else condition:
age = 15

if age >= 18:
    print("You are an adult")
else: # excutes when if fails.
    print("You are a minor")
# 3. elif condition:
# Use elif (else if) when you have multiple conditions to check in sequence.
marks = 72

if marks >= 90:
    print("Grade: A")
elif marks >= 75:# execute when if fails but there is/sre other conditions to check.
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:#executes when all the conditions fails.
    print("Grade: F")
# Important: Python checks conditions top to bottom and stops at the first True condition. Order matters!
# ❌ Wrong order — this bug is common (you had this exact issue in your chatbot!)
score = 95
if score >= 40:
    print("D")      # This runs first and exits — wrong!
elif score >= 90:
    print("A")       # Never reached

# ✅ Correct order — most specific/highest condition first
score = 95
if score >= 90:
    print("A")        # Correctly runs
elif score >= 40:
    print("D")