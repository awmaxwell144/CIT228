# Write your code here :-)
class Privileges(): # for 9-8
    def __init__(self, privileges=[]):
        self.privileges = privileges
    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")
