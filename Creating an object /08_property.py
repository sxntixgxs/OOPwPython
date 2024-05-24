# Properties are like methods that are able to interact with private methods or attributes while mantain the encapsulation principle.

# In practice, what property does is insted calling a setter or getter with a method notation, this allows us to use it the same getter, setter or deletter as a PROPERTY.

# So, this is an example:


class User:
    def __init__(self,nick,password,phone):
        self.__nick = nick
        self.__password = password
        self.__phone = phone
    def get_name(self):
        print(self.__nick)

user1 = User("diavlo","321","32154376")

user1.get_name() # This is the classic way, whit all this code I get the nickname.

# But I can use the @Property to stablish getters without calling them as functions and calling it 'get' is needless 

class Artist:
    def __init__(self,name,password,phone,charts):
        self.__name = name
        self.__password = password
        self.__phone = phone
        self.__charts = charts
    @property #Here I created the decorator and this allow me to use the following function as a PROPERTY but don't allow change its value
    def name(self):
        print(self.__name)
artist1 = Artist("Akapellah","911","321223","Venezuelan Top 50")
artist1.name 
# Si se trata de cambiar el valor de esta forma
# artist1.name = "elvago" 
# Arroja este error
# Traceback (most recent call last):
#   File "/home/camper/Documentos/Sandoval/OOPwPython/Creating an object /08_property.py", line 33, in <module>
#     artist1.name = "elvago"
# AttributeError: can't set attribute 'name'