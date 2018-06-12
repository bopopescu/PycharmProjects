class Parent:

    def __init__(self,name,model):
        self.name = name
        self.model = model

    def displayProfile(self):

        return "Name:{0}\n Model:{1}" .format(
            self.name,
            self.model
        )

class Child(Parent):

    def setModel(self,city):
        self.city = city


    def displayProfile(self):  # method of parent class

        return "Name:{0}\nModel:{1}\nCity:{2}".format(
            self.name,
            self.model,
            self.city
        )

obj = Child("swift","suzuki")
obj.setModel("dddd")
temp = obj.displayProfile()
print(temp)
