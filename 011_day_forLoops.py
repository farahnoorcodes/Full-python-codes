# Day 4: For Loops

# Basic for loop with range()
# range() generates a sequence of numbers — it doesn't create a full list in memory, just gives you numbers one at a time as the loop asks for them
# range(stop)              # 0 to stop-1              #stop is always excluded — this trips people up a lot, so watch for it in your Fizz exercise (range 1 to 20 means range(1, 21), not range(1, 20)).
# range(start, stop)       # start to stop-1
# range(start, stop, step) # start to stop-1, jumping by step
range(5)          # 0, 1, 2, 3, 4        (5 numbers, stops BEFORE 5)
range(2, 7)        # 2, 3, 4, 5, 6        (starts at 2, stops before 7)
range(0, 10, 3)     # 0, 3, 6, 9           (steps by 3)
range(10, 0, -2)    # 10, 8, 6, 4, 2       (counts down)
for i in range(5):
    print(i)  # 0 1 2 3 4

# range(start, stop)
for i in range(1, 6):
    print(i)  # 1 2 3 4 5

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0 2 4 6 8

# looping backwards
for i in range(10, 0, -1):
    print(i)  # 10 9 8 ... 1

# looping through a string
name = "Farah"
for letter in name:
    print(letter)

# using if/elif inside a loop (combining with what you already know)
for num in range(1, 11):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

