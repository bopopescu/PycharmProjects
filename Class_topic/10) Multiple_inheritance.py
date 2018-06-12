# Multiple inheritance A > B >> C

class A: # child class of A

    def __init__(self,a): # constructor of child class A
        self.a = a

    def getA(self): # getA method of child  class A
        return self.a

    def display(self): # display method of child Class A
        return "A:{0}\n" .format(self.a)

class B: # child Class of C

    def __init__(self,b): # constructor of child class B
        self.b = b

    def getB(self): # getB method of child  class B
        return self.b

class C(A,B): # parent class C # parent class calling both child class in C as C(A,B

    def __init__(self,a,b,c):# constructor of parent class C
        A.__init__(self,a) # declaring child class A
        B.__init__(self,b) # declaring child class B
        self.c = c

    def getC(self): # getC method of parent  class C
        return self.c

    def display(self): # display method of Parent Class C
        return "A:{0}\nB:{1}\nc:{2}" .format(
            self.a,
            self.b,
            self.c
        )

c = C(1,2,3)
temp = c.display()
print(temp)