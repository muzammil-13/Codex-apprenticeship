# print("Hello world")

# import sys

# print(sys.version)

# if 5>2:
#     print("5 is less than 2") #statment1
# else:
#     print("3 is less than 5") #statment2

# x=5
# y="Hello world"
# print(x,y)

# Create a variable outside of a function, and use it inside the function
# var1="variable1"

# def myfunc():
#     print("this is ",var1)

# myfunc()

# Create a variable inside a function, with the same name as the global variable
var1="global variable"

def myFunc():
    # If you use the global keyword, the variable belongs to the global scope:
    global var1
    var1="local variable"
    print("This is ",var1)

myFunc()

print("Python is ",var1)