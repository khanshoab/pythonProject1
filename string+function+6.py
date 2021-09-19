# startswith () -This method is used to check whether a string is starting with a substring or not. it
# returns True if the string starts with specified  sub string.

name = "hi How are you shabby"
print(name.startswith("hi"))
print(name.startswith("hii"))

num1 = "hello every one"         # it is case sensitive
hello = num1.startswith("hello")
print(hello)

# endswith () -This method is used to check whether a string is ending with a substring or not.
# It returns True if the string ends with specified sub string.

name = "hi How are you shabby kh"
print(name.endswith("kh"))
print(name.endswith("KH"))

num1 = "hello everyone"         # it is case sensitive
hello = num1.endswith("one")
print(hello)