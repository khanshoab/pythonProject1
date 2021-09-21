# Return statement can be used to return something from the function . in Python , it is possible to return
# one or more variables/values.
# Defining a function
def add():
    a = 10
    b = 20
    c = a + b
    return c


# calling a function
some = add()
print(some)


def abb():
    a = 10
    b = 20
    return a + b


apple = abb()
print(apple)


def abd(b):
    a = 10
    return a + b


ball = abd(20)
print(ball)


def aad(b):
    a = 10
    d = a - b
    g = a + b
    f = a * b
    return d, g, f


pen, paper, hello = aad(20)
print(pen)
print(paper)
print(hello)

