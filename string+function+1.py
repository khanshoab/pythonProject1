# isupper () This method is used to test whether given string is in upper case or not , it returns
# True if string contains at least one letter and all character are in upper case else returns False
name = "KHAN SHABBY"
print(name.isupper())
str1 = name.isupper()
print(str1)
value = "KHAN SHaBBY"   # here one letter is small
print(value.isupper())

# islower () This method is used to test whether given string is in lower case or not , it returns
# True if string contains at least one letter and all character are in lower case else returns False
name = "khan shabby"
print(name.islower())
str1 = name.islower()
print(str1)
value = "khan shaBby"   # here one letter is capital
print(value.islower())


# istitle () This method is used to test whether given string is in title case or not , it returns
# True if string contains at least one letter and each word of the string starts with a capital letter False
name = "Khan Shabby India Mumbai"
print(name.istitle())
str1 = name.istitle()
print(str1)
value = "Khan Shabby india Mumbai"   # here one letter is small
print(value.istitle())
