# User is the class, in OOP a class is the blueprint for all the Users in this case.

class User:
    def __init__(self, nickname, password, email, phone):
        self.nickname = nickname
        self.password = password
        self.email = email
        self.phone = phone
    def print_attributes(self):
        print(f'USER: {self.nickname}\n\n These are all their attributes:\n\n PASSWORD: {self.password}\n EMAIL: {self.email}\n PHONE: {self.phone}')
# this is the constructor function for the class User, now let's create an instance...

user0 = User("admin","admin123","sandovalbgasantiago@gmail.com","+573242442868")

# If you want to print all the attributes of the instance you have to use __dict__ method. 
# For having in account this method just print the attributes that have been assinged explicitly. All the native attributes or methods will be ignored - Ex: __self__

print(user0.__dict__)