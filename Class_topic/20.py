#class  decorator

#static mathod

'''class A:

    def __init__(self):
        self.name = "xyz"
        self.__email = 'xyz@gmail.com'

    @staticmethod
    def dosmthg(self):
        print("i am dosmthg method")


a = A()
a.dosmthg('abc')
# or
#a.dosmthg(11)

#print(a.name)'''

'''class A:

    def __init__(self):
        self.name = "xyz"
        self.__email = 'xyz@gmail.com'

    @staticmethod
    def dosmthg(a,b):
        print("i am dosmthg method")
        print(a+b)

a = A()
a.dosmthg(1,2)'''

# class method

'''class A:

    def __init__(self,name,email):
        self.name = name
        self.email = email

    @classmethod
    def dosmthg(cls): #cls : class A
        a2 = cls('xyz','xyz@gmail.com') # object : without self
        print(a2.name)
        print(a2.email)

a = A('abc','abc@gmail.com')
a.dosmthg()

print("===========outside class+++++++++++")
print(a.name)
print(a.email)'''
