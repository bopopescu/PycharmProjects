# adding variable to class
'''class A:
    count = 0
    def setData(self,name,counter):
        self.name = name
        A.count += 1
        self.counter = counter


a = A()
a.setData("raju",20)
print(a.count) # output - 1

a2 = A()
a2.setData("raju", 10)
print(a2.count) # output - 2

a3 = A()
a3.setData("raju", 15)
print(a3.count) # output - 3

a8 = A()
a8.setData("raju", 15)
print(a8.count) # output - 4

a4 = A()
a4.setData("raju", 12)
print(a4.count) # output - 5 (because a.count is called 5 times output is 5 ,if u execute only a8 count is 1 time)
'''

# constructor
'''class A:
    def __init__(self):

        print("i am in _init__ of clss A")
        self.name = "raju"
        self.email = "ram@gmail.com"

    def display(self):

        return self.name + '\n' + self.email

a = A()
temp = a.display()
print(temp)'''


# Destructor
'''class A:
    def __init__(self, name, email):

        print("i am in _init__ of class A")
        self.name = name
        self.email = email

    def display(self):

        return self.name + '\t' + self.email

    def __del__(self):
        print("i am here") # last destructor output executes

    def __str__(self):
        return self.name # prints raj


#a = A()
a = A('raj', 'ram@gmail.com')
print(a)
temp = a.display()
print(temp) # displays - raj	ram@gmail.com
print(hasattr(a,'name1')) # checks true or false'''



