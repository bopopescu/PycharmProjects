# import 3 methods

# 1) import  PackageName
'''import test
print(test.email)
test.name()'''

# 2) from PackageName import VarName ,functions ,Classes
'''from test import name,email

name()
print((email))'''

# 3) from PackageName import *
'''from test import *

name()
print(email)'''

# 4) from PackageName import VarName as NewVarNme, ClassName as NewClassName, functionName as NewfunctionName

'''from test import name as newName,email as newEmail

email = "rahul@gmail.com"
def name():
    print("rahul")

newName()
name()

print(email)
print(newEmail)'''