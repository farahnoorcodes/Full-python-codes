#there are some rules of decalaring a variable, they are given below:
# Must-follow rules (or you'll get an error):

# Can only contain letters, numbers, and underscores (_)
# Cannot start with a number
# Cannot contain spaces or special characters (-, @, !, etc.)
# Cannot be a reserved keyword (if, for, class, return, etc.)
# Case-sensitive (age and Age are different variables)

# Best-practice conventions:

# Use snake_case for variable names (lowercase, words separated by underscores)
# Use descriptive names, not single letters (except in short loops)
# Constants are usually written in ALL_CAPS
#  Valid variable names
age = 25
student_name = "Farah"
_temp = 10          # starts with underscore - valid but unconventional
total2 = 50
CGPA = 3.67          # convention for constants

#  Invalid variable names (will cause errors)
2age = 25            # cannot start with a number
student-name = "Ali" # hyphens not allowed
class = "CS"         # 'class' is a reserved keyword
my var = 10          # spaces not allowed

# ✅ Good practice vs ❌ Poor practice
good_practice = "Descriptive name"
x = "Descriptive name"   # works, but unclear what it represents

# Case sensitivity example
name = "Farah"
Name = "Noor"
print(name)   # Farah
print(Name)   # Noor  -> treated as a completely different variable
#Use snake_case (e.g. student_marks, total_price) rather than camelCase (which is more common in JavaScript/Java) — it's the standard convention in Python (PEP 8).