#For apply this feature, we going to create another instance of the class User, in this case, the instance will be for those users that decide to vote on the surveys / charts.

# First of all, we going to import all the requires for save coherence in all the modules.
from libraries.tabulate import tabulate
from create_a_class import User
from inheritance import UserArtist

# The name for this instance going to be UserVoter

class UserVoter(User):
    def __init__(self, nickname, password, email, phone, votes_history):
        super().__init__(nickname,password,email,phone)
        self.user_voter_votes_history = votes_history
    def user_print_attributes(self):
        self.print_attributes()
    def show_votes(self):
# In this case, votes_history is a list of dictionaries where each dictionary contains a key:value pair representing the chart where the user voted and their choice.
# This is the loop for print all the votes

        print("="*20)
        print(f'USER: {self.nickname}\n has voted on the following charts:\n')
        print(tabulate(self.user_voter_votes_history))


votes_history = [["Week","Alcolirykoz"],["Month","Akapellah"],["Year","Luis7Lunes"]]
user3 = UserVoter("diavlo","hi123","diavlo@satanas.co","66666",votes_history)

user3.user_print_attributes()
user3.show_votes()