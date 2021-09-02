# String : string represent the group of character.
# String are the closed in single or double quote.
# The str data type is represent a string.

# double quote inside the single quote
str1 = 'hello "khan bhai" how are you'
print(str1)
print()

# single quote inside the doube quote
str2 = "how 'are you' my friend"
print(str2)
print()

# multiline comment in single quote
str3 = '''hello
how 
are you'''
print(str3)
print()

# multiline comment in double quote
str4 = """hello
my
friend"""
print(str4)
print()

# Memory Allocation
str5 = "khan bhai"
str6 = "khan bhai"
print("str5=",id(str5))
print("str6=",id(str6))

# memory allocation
str7 = "python"
str8 = str7
print("str7=",id(str7))
print("str8=",id(str8))

# memory allocation with different values
str9 = "python is best"  # This value goes to garbage
print("str9=",id(str9))
str9 = "python is not best" # This value is print every time
print("str9=",id(str9))
print(str9)

# index  represent the position no. of the a string
# Accessing character and string
str10 = "CHARACTERISTICS"
print(str10)
print(str10[1])   # To print the first element 'C' index start with always 0
print(str10[5])   # To print the fifth element 'A'
print(str10[-1])  # To print the last element 's' index start with reverse side and it always start with -1
print(str10[-2])  # To print the second last element 'c' index start with reverse side
