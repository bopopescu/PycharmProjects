class Parent:

    def __init__(self,name,model):
        self.name = name
        self.model = model

    def displayProfile(self): # display method in parent class
        return "Name:{0}\nModel:{1}".format(
            self.name,
            self.model
        )

class Child(Parent):

    def __init__(self,name,model,pincode): # constructor of child class
        super(Child, self).__init__(name,model) # parent containing three attributes
        self.pincode = pincode



    def getModel(self):
        return  self.name , self.model ,self.pincode

obj = Child("swift","suzuki","kkk")
temp = obj.getModel()
print(temp)

