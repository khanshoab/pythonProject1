# Pass a Function as Parameter
# We can pass a function as parameter to another function.
# def dish(sh):
#     print("This is dish function" + sh())
#
#
# def fif():
#     return " This is fif function"
#
#
# dish(fif)

# another e.g
def dish(sh):
    return "This is dish function" + sh()


def fif():
    return " This is fif function"


a = dish(fif)
print(a)
