class Profile: # Parent class

    def __init__(self, name, email, address): # constructor of parent class
        self.name = name
        self.email = email
        self.address = address

    def displayProfile(self): # display method in parent class
        return "Name:{0}\nEmail:{1}\nAddress:{2}".format(
            self.name,
            self.email,
            self.address
        )