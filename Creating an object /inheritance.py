# First of all, for use the class previously defined we have to import this file.


from create_a_class import User



# We already have a class created, so the purpose here is to create or define a subclass ussing inheritance.

class UserArtist(User):
    def __init__(self, nickname, password, email, phone, record_label, top_song):
        super().__init__(nickname, password, email, phone)
        self.artist_record_label = record_label
        self.artist_top_song = top_song
    # Now, to facilitate the process, we are going to create a method that prints out all the attributes.
    def print_attributes(self):
        print(f'Artist DATA:\n name: {self.nickname}\n password: {self.password}\n email: {self.email}\n phone: {self.phone}\n record label: {self.artist_record_label}\n top song: {self.artist_top_song}\n')




user1 = UserArtist("Gambeta","az123","prueba@prueba.com","+573242442868","Alcolirykoz","https://shorturl.at/kBGSY")

user1.print_attributes()