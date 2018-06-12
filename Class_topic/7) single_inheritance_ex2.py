# Using Super in Child class  we can alter Parent class attributes like Pincode
# super is like update version of parent class in child class
'''class UserProfile(Profile): # Child Class

    def __init__(self,name,email,address,pincode): # constructor of child Class
        super(UserProfile, self).__init__(name,email,address) # parent containing three attributes
        self.pincode = pincode'''

class Profile: # Parent Class

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

class UserProfile(Profile): # Child Class

    def __init__(self,name,email,address,pincode): # constructor of child class
        super(UserProfile, self).__init__(name,email,address) # parent containing three attributes
        self.pincode = pincode

    def setCity(self, city): # setCity method of child lass
        self.city = city


    def displayProfile(self): # display method in child class
        return "Name:{0}\nEmail:{1}\nAddress:{2}\nCity:{3}\nPincode:{4}".format(
            self.name,
            self.email,
            self.address,
            self.city,
            self.pincode
        )


user = UserProfile("Raju","raju@gmail.com","BTM","580045")     # object of child class
user.setCity("Bangalore") # adding attribute value to child class
temp = user.displayProfile()
print(temp)
