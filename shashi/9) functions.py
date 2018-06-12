# Assigment : how to count repeated string in a given sting 18/05/2018
'''m = [1,"hi",3,3,"hi"]
result = {}
for i in m:
    result[i] = m.count(i)
print(result)'''

# functions

# return statement before print
'''def addition(a,b):
    return
    print("i am in addition function")
addition(1,2)'''

# function header
'''def addition(a,b):
    print("i am in addition function")
addition(1,2)'''

# called and calling function
'''def addition(a,b):
    if a == 10:
        return "return 10"
    else:
        return "return 20"
print("aaaa")
print("bbbbbb")
temp = addition(10,2)
print(temp)'''

# function parameter
'''def addition(name ,email):
    return "Name:{0}\nEmail:{1}".format(name,email)
temp = addition(email = 'raj@gmail.com' , name = 'Raj')
print(temp)'''

#fuction arguments

# multiple argument (**a) & (*args,**a)
'''def addition(**a):
    print(a) 
addition(email='raj@gmail.com', name='raj')'''

# single argument (*args)
'''def addition(*args):
    print(args)
addition('raj@gmail.com')'''

'''def addition(*a):
    print(a)
addition('shashi@gmail.com')'''
# multiple argument

'''def addition(*args,**a):
    print(args)
    print(a)
addition(1,2,3,email='raj@gmail.com', name='raj')'''

