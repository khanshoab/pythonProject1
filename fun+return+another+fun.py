# Function return another Function

def first():
    def second():
        return " second function"

    print("first function")
    return second


gg = first()
print(gg())

# Other example
def fhg(may):
    print("This is fgh function")
    return may


def how():
    return "This is how function"


hello = fhg(how)
print(hello())
