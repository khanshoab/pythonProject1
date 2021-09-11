# This method is used to format string The string on which this method is called can contain literal text or
# replacement fields delimited by braces {} Each replacement field contain either the numeric index of a positional
# argument ,or the name of a keyword  argument .

# Integer
print("{}".format(10))
print("{} {}".format(10, 20))
print("{0}".format(10))                              # Note :    do not write space between the {}
print("{0} {1}".format(10, 20))
print("{1} {0}".format(10, 20))
print("{num1}".format(num1=10))
print("{num1} {num2}".format(num1=10, num2=20))
print("{num2} {num1}".format(num1=10, num2=20))
print()

# Float
print("{}".format(10.34))
print("{} {}".format(10.34, 20.34))
print("{}     {}".format(12.12,12.12))
print("{0}".format(10.23))                              # Note :    do not write space between the {}
print("{0} {1}".format(10.23, 20.22))
print("{1} {0}".format(10.23, 20.23))
print("{num1}".format(num1=10.23))
print("{num1} {num2}".format(num1=10.23, num2=20.23))
print("{num2} {num1}".format(num1=10.21, num2=20.21))
print()

# Integer
print("{}".format("khan"))
print("{} {}".format("khan", "khan"))
print("{0}".format("khan"))                              # Note :    do not write space between the {}
print("{0} {1}".format("khan", "bro"))
print("{1} {0}".format("khan", "bro"))
print("{num1}".format(num1="khan"))
print("{str1} {str2}".format(str1="khan", str2="bro"))
print("{str2} {str1}".format(str1="khan", str2="bro"))
print()

# String and Integer
print("where are you going {}".format("khan"))
print("{}hello my name is khan shabby i am from india {}".format("khan", "khan"))
print("{0}".format("khan"))                              # Note :    do not write space between the {}
print("{0} {1}".format("khan", 2368))
print("{1} {0}".format(716, "bro"))
print("{num1}".format(num1="khan"))
print("{str1} {num2}".format(str1="khan", num2=271))
print("{str1} {num2}".format(str1="khan", num2=28))
print()

# Integer
print("{}".format(26))
print("{:d}".format(26))
print("{0:d}".format(26))
print("{num:d}".format(num=26))
print()

# Integer
print("{num:d}".format(num=53))
print("{num:5d}".format(num=53))
print("{num:05d}".format(num=53))
print("{num:+5d}".format(num=53))
print("{num:<5d}".format(num=53))
print("{num:*<5d}".format(num=53))
print("{num:*>5d}".format(num=53))
print("{num:^5d}".format(num=53))
print("{num:*^5d}".format(num=53))
print()

# Float
print("{}".format(32.23))
print("{:f}".format(32.23))
print("{0:f}".format(32.23))
print("{num:f}".format(num=32.23))
print()

# Float
print("{num:f}".format(num=22.21))
print("{num:8f}".format(num=22.21))
print("{num:8.2f}".format(num=22.21))
print("{num:+8.3f}".format(num=22.21))
print("{num:<8.3f}".format(num=22.21))
print("{num:*<8.3f}".format(num=22.21))
print("{num:*>8.3f}".format(num=22.21))
print("{num:^8.3f}".format(num=22.21))
print("{num:*^8.3f}".format(num=22.21))
print()

# String
print("{:8s}".format("khan"))
print("{:<8s}".format("khan"))
print("{:*<8s}".format("khan"))
print("{:>8s}".format("khan"))
print("{:*>8s}".format("khan"))
print("{:^8s}".format("khan"))
print("{:*^8s}".format("khan"))
print()

# String Truncating
print("{:.3s}".format("khan shabby"))
print("{:<8.3s}".format("khan shabby"))
print("{:*<8.3s}".format("khan shabby"))
print("{:>8.3s}".format("khan shabby"))
print("{:*>8.3s}".format("khan shabby"))
print("{:^8.3s}".format("khan shabby"))
print("{:*^8.3s}".format("khan shabby"))
print()

#
print("{:,}".format(21343686358721))
print("{:-}".format(21343686358721))
name = "khan"
age = 20
print("My name is {} and age {}".format(name, age))
a = 30
b = 40
print("{:.2}".format(a/b))
print("{:.2%}".format(a/b))

value = (12,23)
print("{0[0]} {0[1]}".format(value))

data = {"hello":232,"lambda":6718}
print("{0[hello]} {0[lambda]}".format(data))
print("{d[hello]:d} {d[lambda:d]}".format(d=data))
print("{hello} {lambda}".format(**data))


