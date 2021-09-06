# Three type of formatting string
# C-style formatting
# format () Method
# f-String / formatted string literals


# C -style string formatting
# This operator is used to fomatting the string . It interpretes the left argument much like a sprint() style format
# string  to be applied to the right argument , and returns the string resulting from this formatting operation.
# syntax ("formatted placeholder"%(data))

print("%d" % 432)
print("%d %d" % (432,326))
print("%f" % 432.236)
print("%f %f" % ( 432.32,32.123))
print("%f" % 432.232314)
print("%f" % 432.123456432)
print("%s" % "khan bhai")
print("%s %s" % ("hello", "everyone"))
print("%d %s" % (236,"hello everyone"))
# print("%d %s" % ("hello",3728))      # it gives error because we are give opposite value

# We can also write in this way
a = "%d" % 632
print(a)
print(type(a))
# flags using
print("%d" % 348)
print("%+d" % 348)
print("%     d" % 348)   # take only one space
print("%8d" % 437)

print("%f" % 327.722)
print("%3f" % 643.322)   # not required extra three digit
print(f"{643.322:2f}")
print("%2f" % 643.322)

print("%09.2f" % 352.232)

print("%8d" % 325)
print("%08.f" % 326.231)
print("%.f" % 326.231)
print("%08.3f" % 326.231)
print("%09.2f" % 326.231)
print("")
print("%08.f" % 326575867.231)

print("my car no is %d" % 372)
print("my car no is %d given by company" % 372)

a = "my car no is %d given by company" % 328
print(a)
