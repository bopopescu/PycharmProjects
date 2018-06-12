'''class A:

    def __init__(self):

        self.name = "xyz"
        self.__email = 'xyz@gmail.com'


    def getEmail(self):

        return self.__email

a = A()
print(a.name)

#print(a.__email) # error occurs

print(a.getEmail())'''


'''class A:

    def __init__(self):
        self.name = "xyz"
        self.__email = 'xyz@gmail.com'

    def __display(self):

        return "Name:{0}\nEmail:{1}\n" .format(self.name,self.__email)

    def getEmail(self):
        return self.__display()


a = A()
print(a.name)

print(a.getEmail())'''

#print(a.dispaly()) # error occurs