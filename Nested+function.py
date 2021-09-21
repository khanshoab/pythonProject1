# When we define one function inside another function , it is known as Nested Function or Function Nesting.
# Nested Function
# def deep():
#     def more():
#         print(" it is more function")
#     print("This is deep function")
#     more()
#
#
# deep()


# def deep():
#     def more():
#         return "more function"
#     result = more() + " deep function"
#     return result
#
#
# a = deep()
# print(a)

# with parameter
def deep(dp):
    def more():
        return "more function"
    result = more() + dp + " deep function"
    return result


a = deep(" hello this is function")
print(a)





