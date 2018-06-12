# Single Inheritance A >> B
# constructor assigning attribute
'''  def __init__(self, name, email, address): # constructor of parent class
        self.name = name
        self.email = email
        self.address = address'''

class Profile:  # Parent Class

    def __init__(self, name, email, address): # constructor of parent class
        self.name = name
        self.email = email
        self.address = address

    def displayProfile(self): # display method of parent class
        return "Name:{0}\nEmail:{1}\nAddress:{2}".format(
            self.name,
            self.email,
            self.address
        )

class UserProfile(Profile):  # Child Class
    pass # don't take any action

user = UserProfile("Raju","raju@gmail.com","BTM")   # object of child class
temp = user.displayProfile()
print(temp)
