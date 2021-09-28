# Keyword arguments
# These arguments are passed to yhe function with name -value pair to keyword arguments can identify the formal
# arguments by their names.
# The keyword arguments name and formal arguments name must match.
# Note - Number of arguments must be equal in formal and actual arguments ,not more not less.

def show(name, age):
    #  print(name, age)
    print(f"Name: {name} Age: {age}")


show(name="khan",age=21)  # order maintenance is not necessary
