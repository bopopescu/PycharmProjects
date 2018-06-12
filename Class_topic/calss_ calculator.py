class Cal():

    def Info(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b


while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    userObj = Cal() #
    choice = 1
    print("Select Choice : 1)Add , 2)Subtract , 3)Multiply , 4)Divide 5)Exit")

    while choice != 0:
        choice = input("Enter choice(1/2/3/4/5):")
        userObj.Info(a,b) #

        if choice == 1:
            print(userObj.add())
            break
        elif choice == 2:
            print(userObj.sub())
            break
        elif choice == 3:
            print(userObj.mul())
            break
        elif choice == 4:
            print(userObj.div())
            break
        elif choice == 5:
            exit()
        else:
            print("please Enter a correct choice")

