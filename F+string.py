# A formatted string literal or f-string literal that is prefixed with f or F.
# These string may contain replacement fields , which are expression delimited by curly braces {}.
# While other string literal always have a constant value,formatted string are really expression evaluated at run time.
# Integer
a = 13
b = 23
value = f"{a} {b}"
print(value)
print(f"{a}")
print(f"{a} {b}")
print(f"{b} {a}")
print()

# Float
a = 10.11
b = 10.333
value = f"{a} {b}"
print(value)
print(f"{a}")
print(f"{a} {b}")
print(f"{b} {a}")
print()

# String
f_name = "khan"
l_name = "shabby"
print(f"{f_name}")
print(f"{l_name} {f_name}")
print(f"{f_name} {l_name}")
print()

# Integer and String
name = "khan"
age = 20
print(f"Hello my name is {name}")
print(f"{name} {age}")
print(f"{age} {name}")
print()

# Integer
num = 10
print(f"{num}")
print(f"{num:d}")
print(f"{num:5d}")
print(f"{num:05d}")
print(f"{num:+5d}")
print(f"{num:<5d}")
print(f"{num:*<5d}")
print(f"{num:*>5d}")
print(f"{num:^5d}")
print(f"{num:*^5d}")
print()

# Float
num = 10.23
price = 10.329791763199
print(f"{num:f}")
print(f"{price:.20f}")
print(f"{num:5f}")
print(f"{num:05f}")
print(f"{num:+5f}")
print(f"{num:<5f}")
print(f"{num:*<5f}")
print(f"{num:*>5f}")
print(f"{num:^5f}")
print(f"{num:*^5f}")
print()

# String
name = "khan"
print(f"{name}")
print(f"{name:s}")
print(f"{name:<8}")
print(f"{name:*<8}")
print(f"{name:>8}")
print(f"{name:*>8s}")
print(f"{name:^8s}")
print(f"{name:*^8s}")
print()

# String Truncating
name = "shabby"
print(f"{name}")
print(f"{name:*<8.3s}")
print(f"{name:>8.3s}")
print(f"{name:^8.3s}")
print(f"{name:*^8.3s}")
print(f"{name:*^8.6s}")
print()

# #########################
price = 1654651265461517
print(f"{price:,}")
print(f"{price:_}")
name = "shabby"
age = 20
print(f"My name is {name} and age is {age}")
print(f"{10 * 8}")
a = 40
b = 20
print(f"{a / b:.2}")
print(f"{a / b:.5%}")

value = (10, 20)
print(f"{value[0]}")
print(f"{value[1]}")

data = {'khan': 282, 'shabby': 623, 'hello': 273}
print(f"{data['khan']:d} {data['hello']}")

name = "characteristic"
print(f"{name.upper()}")
print(f"{name.lower()}")

# Date and time
from datetime import datetime
today = datetime(2021,8,18)
print(f"{today}")
print(f"{today:%d-%b-%y}")
print(f"{today:%d\%b\%y}")
print(f"{today:%d %b,%y}")