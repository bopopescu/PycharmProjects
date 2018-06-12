# Child Class
# calling Parent class using importing
# importing classes from Parent class using -  from Single_inheritance_Parent_class import Profile
# syntax : from pythonfile name import parent class name
from Single_inheritance_Parent_class import Profile

class UserProfile(Profile): # child class
# defining setCity in Child class

    def setCity(self, city): # setcity method in child class
        self.city= city


    def displayProfile(self): # display method in child class
        return "Name:{0}\nEmail:{1}\nAddress:{2}\nCity:{3}".format(
            self.name,
            self.email,
            self.address,
            self.city
        )


user= UserProfile("Raju","raju@gmail.com","BTM")   # object of child class
user.setCity("Bangalore") # assigning attribute to child class
temp=user.displayProfile()
print(temp)

