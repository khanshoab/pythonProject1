# String are immutable object which means it's value or content can not be changed.
str1 = "father"
print(str1)
for i in str1:
    print(i)
print()
# when try to changed the element
str2 = "father"
# str3 = "python"    # We can resign the value
str2[4] = 'i'  # TypeError: 'str' object does not support item assignment
for i in str2:
    print(i)