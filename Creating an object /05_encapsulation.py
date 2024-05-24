# Doc that explains the concept: https://www.geeksforgeeks.org/encapsulation-in-python/

# The main idea is to protect important or private data within a class from any unauthorized modification or alteration. This is achieved by declaring certain methods and variables as private, ensuring that they only interact within the class itself


# Another feature to add is the encapsulation tries to save or hide the REAL variable name but no the value that's why you can obtain it or manipulate it by getters and setters functions.
#################################################################################

# Protected members: These are built into other languages like C# or Java by default. It means that other classes cannot directly access them, but subclasses are able to do so
# To apply this concept in Python, you just have to prefix the method or variable by an underscore "_"

# This is an example 

"""
Uncomment the following for execute this example
class Base:
    def __init__(self):
        self._a = "Hi, I am private"  # Using the underscore prefix to indicate that the variable is protected or private.

#Now, we are going to use the protected variable through a subclass

class Child(Base):
    def __init__(self):
        # Calling constructor of Base
        Base.__init__(self)
        # print("This is the protected variable called from a subclass\n\n",self._a)
        # Modifing the protected variable
        self._a = "Hi, I have been modified"
        # print(self._a)

dad = Base()
child = Child()

print(dad._a)
print("="*30)
print(child._a)
""" 
#################################################################################

# Private members: The main difference between them is that the class methods or variables declared as private member should not be accessed outside the class, even by a subclass
# NOTE: However, in Python, both private and protected members can be accesed outside the class by a subclass. BUT the privates (__) at first returns an error. However, by a complex series of proccess you can get the access.
# You can declare a private member prefixing the name with two underscores "__"

# There is an example:

class Base:
    def __init__(self):
        self.normalAttribute = "Hi, I'm normal"
        self.__privateAttribute = "Hi, I'm private"
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("This is the normal member",self.normalAttribute)
        print("\n\n")
        print("This is the private member",self.__privateAttribute)

obj = Base()
print(obj.normalAttribute)
print(obj.__privateAttribute) # Gives the following ERROR because this is a PRIVATE attribute
"""Traceback (most recent call last):
  File "/home/camper/Documentos/Sandoval/OOPwPython/Creating an object /05_encapsulation.py", line 59, in <module>
    print(obj.__privateAttribute)
AttributeError: 'Base' object has no attribute '__privateAttribute'. Did you mean: '_Base__privateAttribute'?"""

obj2 = Derived()
obj2