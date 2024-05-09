# Getter: Allows access to a private member of a class
# Setter: Allows settings or mutations to a private member of a class

# How it works?

class Text:
    def __init__(self,font,content):
        self.__font = font
        self.__content = content
    # With this **getter** we can get access to a private attribute since a public method
    def get_content(self): 
        return self.__content
    # With this **setter** we are changing the value of the private attribute __content
    def set_content(self,new_content):
        self.__content = new_content
    def get_font(self):
        return self.__font
    def set_font(self,type_font):
        self.__font = type_font


# Getters use:

label = Text("Times New Roman","Kendrick vs Drake disstrack has been converted in the greates on HIP HOP history")
print("We are going to access to the hidden information below\n")
print(f"This is the font of the text {label.get_font()}")
print("")
print(f"This is the content of the TEXT {label.get_content()}")



print("#"*30)

# Setters use:
label.set_font('Arial') #Updating font value
label.set_content('Cosculluela vs Anuel disstrack has been rejected by the majority of their fans') #Updating content value

print(f"This is the updated font:\n {label.get_font()}") # Here we using getters for obtain the data
print("")
print(f"This is the updated content:\n {label.get_content()}")