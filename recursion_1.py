import sys

# Prints 1000 as max recursion
# print(sys.getrecursionlimit())

# Set recursion limit to 2000
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

# def greet():
#     print("Hey!")
#     greet()
#
# greet()

i=0
def greet():
    global i
    i+=1
    print("Hey!",i)
    greet()

greet()