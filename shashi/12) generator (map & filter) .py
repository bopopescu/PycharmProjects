# Generator
'''def testGen():

    yield 1
    yield 2
    yield 3

temp = testGen()

print(temp.__next__())
print(temp.__next__())
print(temp.__next__())'''


'''def testGen():

    #yield 1
    #yield 2
    #yield 3
    #yield "xyz"

    for i in range(1,11):
        yield i * i

temp = testGen()

try:
    while True:
        print(temp.__next__())
except:
     pass'''

# pass show nothing
'''if True:
    pass

def sdf(): 
    pass
'''

# Generator
# map
'''l1 = range(1,6)
data = map(lambda x:x *x ,l1)
print(list(data))'''

'''def sqr(item):
    return item * item

l1 = range(1,6)
data = map(sqr,l1)
print(list(data))'''

'''def sqr(item, item2):
    return item * item2

l1 = [1,2,3,4,5]
#l2 = [10,20,30]
l2 = [10,20,30,40,50,60]
#data = map(sqr,l1,l2)
data = map(lambda x,y:x * y,l1,l2)
print(list(data))'''

# filter
'''l1 = [1,2,3,4,5]

data = filter(lambda x:x%2==0,l1)
data = filter(lambda x:x%x if x%2==0 else x,l1)

print(list(data))'''

# Generate a string, convert into uppercase string using lambda and filter function
'''l1 = "hi HELLO hai"
#data = map(lambda x:x.lower(),l1)
#data = map(lambda x:x.upper(),l1)
data = filter(lambda x: x.isupper(),l1)
data = filter(lambda x: x.islower(),l1)
#print("".join(data))
#print(list(data))'''

# filter
'''data = filter(lambda x:x%2==0 ,[1,2,3,4,5])
print(list(data))

# map
data = map(lambda x:x%2==0 ,[1,2,3,4,5])
print(list(data))'''
