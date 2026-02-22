"""
name = "Fernando"
year = 1987
value = 19.99

# This is a line commented

'''
    This is an entire
    Line
    Commented
    With a lot of lines

'''

print("Hello, World!") # That line is already printed with a newline

name = input("Please, type your name: ")

print(f"Your name is {name} and the type is {type(name)}") # We can use format string to put more values

num1 = 2001
print("This is a number test: ", type(num1)) # Everything in Python is a object

# Testing casting

num = input("Type a number: ")
num = float(num) # we can make a direct casting

print(num) # We can see directly the number here
print(type(num))

"""

# Testing Lists

names = ['Fernando', 'Larissa', 'Eduardo', 'Jonas', 'José', 'Maria']
print(names, len(names), names[3])

# Testing operators

num1 = 52
num2 = 106

print(num1 + num2)

result = num1 + num2

print(result)

result = num1 - num2
print (result)

num1 = int(input("Type the first number: ")) #solving the problem with a cast
num2 = int(input("Type the second number: "))

print(f"The sum of {num1} with {num2} is {num1 + num2}")
print(f"The subtraction of {num1} with {num2} is {num1 - num2}")
print(f"The multiplication of {num1} with {num2} is {num1 * num2}")
try:
    print(f"The division of {num1} with {num2} is: {num1 / num2}")
except ZeroDivisionError:
    print("You cannot divide by Zero")

print("{num1} > {num2} is {num1 > num2}")
