# Python allows functions as a variable
# Because of this feature, we can use a function calling it from other variable that stores this function
# Below is an example to be clear



def say(text):
    return text.upper()
yell = say # Using the variable yell to reference the function say
print(yell("hi brah"))

###############################################################################################
# Doc https://www.geeksforgeeks.org/decorators-in-python/
# Decorators are used to modify the behavior of function or class