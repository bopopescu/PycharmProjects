#  Assignments

# Program make a simple calculator that can add, subtract, multiply and divide using functions

# This function adds two numbers
def add(x, y):
   return x + y

# This function subtracts two numbers
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y


while True:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    while num1.isdigit() and num2.isdigit() == True:
        print("Select Choice : 1)Add , 2)Subtract , 3)Multiply , 4)Divide 5)Exit")
        choice = input("Enter choice(1/2/3/4/5):")
        if choice == '1':
            print(num1,"+",num2,"=", add(int(num1),int(num2)))
            break
        elif choice == '2':
            print(num1,"-",num2,"=", subtract(int(num1),int(num2)))
            break
        elif choice == '3':
            print(num1,"*",num2,"=", multiply(int(num1),int(num2)))
            break
        elif choice == '4':
            print(num1,"-",num2,"=", divide(int(num1),int(num2)))
            break
        elif choice == '5':
            exit()
        else:
            print("please Enter a correct choice")
else:
    print("Please Enter a no")

print("hello")

# to print Capital letter from string

'''def upperOnly(s):
    onlyCaps = ""
    for char in s:
        if char.isupper() == True:
            onlyCaps += char
            print("hi")
    return onlyCaps
print("shashi")
print(upperOnly("TeSt"))
print("kumar")'''

# to find largest to four no's using lambda function
'''data = lambda a,b,c,d: a if a > b and a > c and a > d else  b if  b > c and b > d else c if  c > d else d
#print(data)
#print(data()) # error statement
print(data(200,700,9000,6))'''

# to find largest to four no's using lambda function
'''a = input("enter a no")
b = input("enter a no")
c = input("enter a no")
d = input("enter a no")

data = lambda a,b,c,d: a if a > b and a > c and a > d else  b if  b > c and b > d else c if  c > d else d
print(data(a,b,c,d))'''

# comprehension tuple
'''listdata = [1,2,3,4,5]
data = tuple(i * i for i in listdata)
print(list(data))'''

'''squares = tuple(x**2 for x in range(5))
print(squares)'''

'''def sqr(l1):
    temp = []
    for i in l1:
        if i % 2 == 0:
            temp.append(i * i)
        #print(temp)
    #print(temp)
listdata = [1,2,3,4,5]
sqr(listdata)
data = tuple(i * i for i in listdata)
print((data))
data = tuple(i * i for i in listdata  if i % 2 == 0 )
print(data)'''

# Generate a string, convert into uppercase string using lambda and filter function
'''l1 = "hi HELLO hai"
data = map(lambda x:x.upper(),l1)
#data = map(lambda x:x.lower(),l1)
#data = filter(lambda x: x.isupper(),l1)
#data = filter(lambda x: x.islower(),l1)
print("".join(data))'''
