print("Hello, World!")
print("hello world!")
#for writing a comment in python we use the # symbol
#this is a single line comment
"""this 
is a
 multi-line
   comment"""
#use different print statements to print different messages,but for line breaks we can use \n in the print statement
print("Hello,\nWorld!")
#you can write anything in the print statement, but it should be in double or single quotes.
#there are different format specifiers in python, we can use them to format the output of the print statement.
print("The value of x is %d" % 5)#in this case %d is a format specifier for integer values, and 5 is the value that will be printed in place of %d.
print("The value of x is %f" % 5.5)#in this case %f is a format specifier for float values, and 5.5 is the value that will be printed in place of %f.
print("The value of x is %s" % "Hello")#in this case %s is a format specifier for string values, and "Hello" is the value that will be printed in place of %s.
print("The value of x is %d and the value of y is %f" % (5, 5.5))#in this case we are using multiple format specifiers in a single print statement, and we are passing a tuple of values to be printed in place of the format specifiers.
