
class UserInfo:

    def setInfo(self,name,email):

        self.name = name
        self.email = email

    def getInfo(self):

        return  "Name:{0}\nEmail:{1}".format(self.name,self.email)

print("==================== userObj1 ============")

userObj = UserInfo()
userObj.setInfo("raju",'raj@gmail.com')
temp = userObj.getInfo()
print(temp)

print("==================== userObj2 ============")

userObj2 = UserInfo()
userObj2.setInfo("shashi",'shashi@gmail.com')
temp2 = userObj2.getInfo()
print(temp2)
