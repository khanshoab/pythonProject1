# Function are subprograms which ar used to compute a value or perform a task.

# Type of function
# 1. built in function e.g print() , upper(), lower().
# 2. user-defined function
#  ** Advantage of Function **
# write once and use it as many time as you need. This provides code re-usability.
# Function facilities case of code maintenance.
# Divide large task into small task so it will help you to debug code.
# You can remove or add new feature to a function anytime.
# ** Function Definition **
# We can define a function using def keyword followed by function name with parentheses.
# This is also called as Creating a Function, Defining a Function.
# ** Calling A Function **
# A function runs only when we call it, function can not run on its own.
# ** How Function Work **


# write once and use it as many time as you need.
# Defining a Function
def show():
    name = "Independence"
    print("Today is", name)


# Calling a Function
show()


# Diving Large task into many small task, helpful for de-bugging code.
# Defining Function
def add():
    x = 10
    y = 20
    c = x + y
    print(c)


add()


# Separate function for addition
def sub():
    x = 20
    y = 10
    c = x - y
    z = x + y
    m = x * y
    print(c)
    print(z)
    print(m)


sub()


# Function without Argument and Parameter
# Defining a function without Parameter

# no parameter
def hhh():
    a = 10
    b = 20
    c = a + b
    print(c)


# Calling a function without Argument
hhh()


# Calling a function with parameter
def sss(b):
    a = 10
    c = a + b
    print(c)
    print(a + 50)
    print(a + b)
    print(f"Formatted output {a+b:5.2f}")
    print(f"Formatted output {a-b:5.10f}")
    print(f"Formatted output {a*b:5.2f}")


# Calling a function with Argument
sss(20.444)
