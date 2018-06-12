'''single inheritance adding setcity to child class , overriding(using same methods in parent class as well in child
 class ex: def displayProfile(self):'''

class Profile: # Parent Class

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

class UserProfile(Profile): # Child Class
# defining setCity in Child class

    def setCity(self, city): # setCity method of child  class
        self.city = city


    def displayProfile(self): # display method of child  class
        return "Name:{0}\nEmail:{1}\nAddress:{2}\nCity:{3}".format(
            self.name,
            self.email,
            self.address,
            self.city
        )


user = UserProfile("Raju","raju@gmail.com","BTM")   # object of child class
user.setCity("Bangalore") # assigning attribute to child class
temp = user.displayProfile()
print(temp)
