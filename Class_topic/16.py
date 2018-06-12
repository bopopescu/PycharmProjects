class ParentA:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def setInfo(self):
        return complex(self.a) * int(self.b)

class Child:
    pass

obj = ParentA('10','50')
temp = obj.setInfo()
print(temp)