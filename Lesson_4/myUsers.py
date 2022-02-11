# Write your code here :-)
from user import User
from admin import Admin
from privileges import Privileges
print("------------- Exercise 9-3 ---------------")
george = User('George', 'Jetson', 'georgejetson', 'george@jetson.net', 'astro123')
george.describe_user()
george.greet_user()

wilma = User('Wilma', 'Flintstone', 'flinty', 'wilma@flint.net', 'pebbles')
wilma.describe_user()
wilma.greet_user()

print("------------- Exercise 9-5 ---------------")
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
