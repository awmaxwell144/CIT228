# Write your code here :-)
from user import User
from privileges import Privileges
class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()
    def show_privileges(self): #for 9-7
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)
