#Nested function

'''def func1():
    def func2():
        return "hello"
    return func2
data = func1()
print(data())'''

#global function

'''a = 100
def test():
    global a # ti use a value in function
    a = a + 1
    print(a)

#print(a)
test()'''

'''a = 100
def test():
    global a # ti use a value in function
    b = 100
    a = a + 1
    print(a)

#print(a)
test()
print(b)'''

# doc string / documentation function

'''def add(a,b):
    # """ enter then the it will execute :param a:
    #     :par b:
    #     :return:am
    """
    :param a:
    :par b:
    :return:am
    """

    return a + b
print(add.__doc__)
add(1,2)'''

# default parameter intialization

'''def add(a,b = 100):
    return a + b
temp = add(1)
print(temp)'''

# closure function

'''def func1(a):
    def func2(b):
        return "iam function2"
    def func3(c):
        return "i am from func3"
    return [func2,func3]
data = func1(11)
#print(data[0])
#print(data[1])

print(data[0](11))
print(data[1](11))'''


'''def test(a,b):
    if a > b:
        return" ai s largest"
    else:
        return "b is largest"

large = test(10,20)
print(large)
print("============")'''

#lamda - terinary expression : True if condition False

#lambda p1,p2,pn:expression
#exp ? value1 : value2

# to find largest to two no's using lambda function

'''data = lambda a,b: 'a is largest' if a > b else "b is largest"
#print(data)
#print(data()) # error statement
print(data(200,300))'''

# to find largest to three no's using lambda function

'''data = lambda a,b,c: a if a > b and a > c else  b if b > c  else c
#print(data)
#print(data()) # error statement
print(data(2000,3000,500))'''

# to find largest to four no's using lambda function

data = lambda a,b,c,d: a if a > b and a > c and a > d else  b if  b > c and b > d else c if  c > d else d
#print(data)
#print(data()) # error statement
print(data(200,700,9000,6))


