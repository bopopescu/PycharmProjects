# simple calculator program
a = input("Enter a first no : ")
b = input("Enter a second no : ")
if a.isdigit() and b.isdigit() == True:
    print("Select Choice : 1)Add , 2)Subtract , 3)Multiply , 4)Divide")
    select = input("Enter Choice (1/2/3/4): ")
    if select == "1":
        print("Addition of two no's : ",a,"+", b ,"=",int(a) + int(b))
    elif select == '2':
        print("Subtraction of two no's : ",a,"-", b ,"=",int(a) - int(b))
    elif select == '3':
        print("Multiply of two no's : ",a,"*", b ,"=",int(a) * int(b))
    elif select == '4':
        print("Division of two no's : ", a, "/", b, "=", int(a) / int(b))
    else:
        print("please Enter a correct choice")
else:
    print("Please Enter a no")

print("hello")



# isinstance

'''s1 = "Python is east to learn"

if s1.startswith("Python"):
    print("string starts with python")
else:
    print("String does not starts with python")

print(isinstance(s1,str))
print(type(s1))'''

'''s2 = "hello"
print(isinstance(1,int) == True)
print(isinstance(s2,str))
print(isinstance(1,int))
print(type(s2))
print(isinstance("hello",int))'''

# Assigment : how to remove list with in list 20/05/2018

'''temp = []
def extraitem(l1):
    for i in l1:
        if isinstance(i,list):
            extraitem(i)
        else:
            temp.append(i)

listdata = [1,[22,33],44,[[55]],66]
extraitem(listdata)
print(temp)'''

# Assigment : take input find max value in list

'''size = input("size")
l1 = []
while size:
    num = input("number")
    if num.isalpha():
        break
    l1.append(int(num))
    size -=1

max = l1[0]
for i in l1:
    if i > max:
        max = i

print(max)'''

# Assigment : how to count no of string in a given sting

'''string = 'hi how are you'
data = string.split(" ")
d1 = {}
for word in data:
    d1[word] = data.count(word)
print(d1)'''

'''l1 = ['hi','hello', 'hi']
d1 = {}
for word in l1:
    d1[word] = l1.count(word)
print(d1)'''

# highest no in list
'''s = [77,48,19,17,93,90]
a = s[0]

def highestno(s):
    for num in s:
        if num < a:
            a = num
    return a
print(a)'''

