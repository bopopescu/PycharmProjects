# Multilevel inheritance A >> B >> C
# using Super class in Child Class B & C both

class A: # parent class A

    def __init__(self,a): # constructor of parent class
        self.a = a

    def getA(self): # getA method of parent class
        return self.a

    def display(self): # display method of parent class
        return "A:{0}\n" .format(self.a)

class B(A): # child class B # Class B is parent of A

    def __init__(self,a,b): # constructor of child class using super
        super(B, self).__init__(a)
        self.b = b

    def getB(self): # getA method of child class
        return self.b

    def display(self): # display method of child class # in return statement using super
        return "A:{0}\nB:{1}\n" .format(self.a,self.b)

class C(B): # child class C # Class C is parent of B & A both

    def __init__(self,a,b,c): # constructor of child class using super
        super(C,self).__init__(a,b)
        self.c = c

    def getC(self): # getA method of child class
        return self.c

    def display(self): # display method of child class # in return statement using super
        return "A:{0}\nB:{1}\nc:{2}" .format(
        self.a,
        self.b,
        self.c
        )

c = C(1,2,3)
temp = c.display()
print(temp)

