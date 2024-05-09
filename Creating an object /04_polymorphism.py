# Polymorphism concept refers to the feature that allows different classes to use the same method, but with different results.



# Since we are working on the same project, in order to utilize this OOP property, we are going to stablish
# We are going to add the same method a two different classes like User and UserArtist

# The following classes are updated.

class User:
    def __init__(self,nickname,password,email,phone):
        self.nickname = nickname
        self.password = password
        self.email = email
        self.phone = phone
    def print_attributes(self):
        print(f'USER: {self.nickname}\n\n These are all their attributes:\n\n PASSWORD: {self.password}\n\n EMAIL: {self.email}\n\n PHONE: {self.phone}')
    #the following is the new method
    def vote(self,artist,chart):
        print("Your vote has been saved")
        print("This vote is going to be stored in the normal votes list")            
        print(f'You just vote for {artist} on the {chart} chart')

class Artist(User):
    def __init__(self,nickname,password,email,phone,record_label,top_song):
        super().__init__(nickname,password,email,phone)
        self.artist_record_label = record_label
        self.artist_top_song = top_song
    def print_attributes(self):
        print(f'USER: {self.nickname}\n\n These are all their attributes:\n\n PASSWORD: {self.password}\n\n EMAIL: {self.email}\n\n PHONE: {self.phone}\n\n RECORD LABEL: {self.artist_record_label}\n\nTOP SONG: {self.artist_top_song}')
    #This is the polymorphism method (?)
    def vote(self,artist,chart):
        print("Your vote has been saved")
        print("This vote is going to be stored in the artist votes list")            
        print(f'You just vote for {artist} on the {chart} chart')

# Now, let's try it

ordinary_user = User("ordinary_user","1234","ordinary@user.net","+3213456")

artist_user = Artist("artist_user","1234","artist@user.net","+9846543","InfinityMusic","Meet the Grahams")


ordinary_user.vote("Kendrick Lammar","Top Week")
print("")
print("")
print("*"*50)
print("")
print("")

artist_user.vote("Drake","Top Year")


    