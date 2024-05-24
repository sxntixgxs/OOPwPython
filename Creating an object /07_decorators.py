# # Python allows functions as a variable
# # Because of this feature, we can use a function calling it from other variable that stores this function
# # Below is an example to be clear



# def say(text):
#     return text.upper()
# yell = say # Using the variable yell to reference the function say
# print(yell("hi brah"))

# ###############################################################################################
# # Doc https://www.geeksforgeeks.org/decorators-in-python/
# # Decorators are used to modify the behavior of function or class


# # Bellow is the example of how a decorators works

# def decorator(function):
#     print("Hi I'm in the decorator and this is before the outside function")

#     function()

#     print("Hi, I'm in the decorator and this occur after all.")



# def function_to_be_used():
#     print("I'm the outside (?) function")

# decorator(function_to_be_used)

# What actually decorators do is modify by "improving" or adding some funtionality to a existing function but mantain a clean code.

# However, the first example was not totally right. We can exploit the decorators potential using it with a line that references the actual decorator when  function to be used has called.
# This example shows it.

def decorator2(func):
    print("I'm first hehe")

    func()

    print("I'm lastest :(")
def function_to_be_used2():
    print("I'm the MAIN function btw")

#Here we should update the function doing this
function_to_be_used2 = decorator2(function_to_be_used2)
#So when we call the same function along the program that already exists just change the result

function_to_be_used2

# But, the best way to do this is the following:

def decorator3(func):
    print("This is the best example :D")
    func()
    print("And this is all :(")
@decorator3
def function_to_be_used3():
    print("I'm the actual important function")
function_to_be_used3

