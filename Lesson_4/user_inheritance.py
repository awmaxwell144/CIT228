# Write your code here :-)
# Write your code here :-)
print("------------- Exercise 9-3 ---------------")
"""Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are
typically stored in a user profile. Make a method called
describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized
greeting to the user. Create several instances representing different
users, and call both methods for each user.
"""
class User():

    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Password: " + self.password)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

george = User('George', 'Jetson', 'georgejetson', 'george@jetson.net', 'astro123')
george.describe_user()
george.greet_user()

wilma = User('Wilma', 'Flintstone', 'flinty', 'wilma@flint.net', 'pebbles')
wilma.describe_user()
wilma.greet_user()

print("------------- Exercise 9-5 ---------------")
"""Add an attribute called login_attempts to your User class from
Exercise 9-3 (page 162). Write a method called increment_login
_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets
the value of login_attempts to 0. Make an instance of the User
class and call increment_login_attempts() several times. Print
the value of login_attempts to make sure it was incremented properly,
and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0."""

print(f'Wilma has tried to log in {str(wilma.login_attempts)} times!' )
wilma.increment_login_attempts()
print(f'Wilma has tried to log in {str(wilma.login_attempts)} times!' )
wilma.increment_login_attempts()
print(f'Wilma has tried to log in {str(wilma.login_attempts)} times!' )
wilma.increment_login_attempts()
print(f'Wilma has tried to log in {str(wilma.login_attempts)} times!' )
print('Wilma, you have exceeded the number of login attempts')

print("Resetting login attempts...")
wilma.reset_login_attempts()
print("Login attempts has been reset to: " + str(wilma.login_attempts))
print('Your account will be locked for 5 minutes')

print("------------- Exercise 9-7 & 9-8 ---------------")
"""9-7: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3
(page 162) or Exercise 9-5 (page 167). Add an attribute, privileges,
that stores a list of strings like "can add post", "can delete post",
"can ban user", and so on. Write a method called show_privileges()
that lists the administrator’s set of privileges. Create an instance
of Admin, and call your method."""
"""9-8: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in
Exercise 9-7. Move the show_privileges() method to this class. Make a
Privileges instance as an attribute in the Admin class. Create a new
instance of Admin and use your method to show its privileges.
"""
class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()
    def show_privileges(self): #for 9-7
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)

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

betty = Admin('betty', 'Rubble', 'bets', 'bets@rub.com', 'bambam')
betty.describe_user()
betty.privileges.show_privileges()

print("\nAdding privileges...")
betty_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
betty.privileges.privileges = betty_privileges
betty.privileges.show_privileges()

