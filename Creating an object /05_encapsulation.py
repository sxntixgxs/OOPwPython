# Doc that explains the concept: https://www.geeksforgeeks.org/encapsulation-in-python/

# The main idea is to protect important or private data within a class from any unauthorized modification or alteration. This is achieved by declaring certain methods and variables as private, ensuring that they only interact within the class itself

# Protected members: These are built into other languages like C# or Java by default. It means that other classes cannot directly access them, but subclasses are able to do so
# To apply this concept in Python, you just have to prefix the method or variable by an underscore "_"

# This is an example 

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
