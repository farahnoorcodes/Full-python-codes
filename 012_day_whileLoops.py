#A while loop in Python repeats a block of code as long as a condition stays true.
# while condition:
    # code to repeat
# example: 
count = 0
while count < 5:
    print(count)
    count += 1
# output: 
# 0
# 1
# 2
# 3
# 4
# Key parts

# Condition: checked before each loop run. If it's False at the start, the loop body never runs.
# Loop body: must eventually change something that affects the condition, or you'll get an infinite loop.

# Infinite loop (intentional)
while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input == "exit":
        break
# Here break exits the loop manually.
# continue
# Skips the rest of the current iteration and goes back to checking the condition:
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
# Output: 1 2 4 5 (3 is skipped)
# while with else
# The else block runs if the loop finishes normally (not via break):
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop finished")