'''single inheritance adding setcity to child class , overriding(using same methods in parent class as well in child
 class ex:def displayProfile(self):'''

class Profile: # parent class

    def __init__(self, name,email,address): # constructor of parent class

        self.name = name
        self.email = email
        self.address = address

    def displayProfile(self): # method of parent class

        return "Name:{0}\nEmail:{1}\nAddress:{2}".format(
            self.name,
            self.email,
            self.address
        )
class UserProfile(Profile): # child class

    def setCity(self,city): # setCity method of child class
        self.city = city

    def setEmail(self): # setEmail method of child class
        # overriding setEmail in parent class contructor
        return self.email

    def displayProfile(self): # method of child class

        return "Name:{0}\nEmail:{1}\nAddress:{2}\nCity:{3}".format(
            self.name,
            self.email,
            self.address,
            self.city
        )


userProfile = UserProfile("Raju", "ram@gmail.com","btm")
userProfile.setCity("bangalore")
temp = userProfile.displayProfile()
print(temp)