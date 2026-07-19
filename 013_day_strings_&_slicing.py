# A string in Python is a sequence of characters used to represent text. It's one of Python's built-in data types, and it's immutable — meaning once created, a string's contents can't be changed in place (any "modification" actually creates a new string).
# Creating strings
# You can define a string using single quotes, double quotes, or triple quotes:
name = 'Farah'
greeting = "Hello, world!"
paragraph = '''This is a
multi-line string.'''
# Single and double quotes work the same way — the choice is mostly style preference (though useful if your text itself contains one type of quote).
# Key characteristics

# Ordered – characters have a defined position (index), starting at 0
# Indexable – you can access individual characters: name[0] → 'F'
# Immutable – you can't do name[0] = 'X'; you'd need to create a new string instead
# Iterable – you can loop through each character with a for loop
# Slicing:
# Slicing lets you extract a portion (substring) of a string using index positions, without changing the original string (remember, strings are immutable).
# basic syntax:
# string[start:stop:step]
# start – index to begin at (inclusive) — default is 0
# stop – index to end at (exclusive) — default is end of string
# step – how many characters to skip each time — default is 1
word = "Python"

print(word[0:2])    # 'Py'   → characters at index 0 and 1
print(word[2:])     # 'thon' → from index 2 to the end
print(word[:4])     # 'Pyth' → from start to index 3
print(word[:])      # 'Python' → the whole string (a copy)
# Using negative indices:
# Negative numbers count from the end of the string:
word1 = "Python"

print(word1[-1])     # 'n'    → last character
print(word1[-3:])    # 'hon'  → last 3 characters
print(word1[:-1])    # 'Pytho' → everything except the last character
# Using step:
word2 = "Python"

print(word2[::2])    # 'Pto'   → every 2nd character
print(word2[::-1])   # 'nohtyP' → reverses the string!
# A useful trick: word[::-1] is a common shortcut for reversing a string.
