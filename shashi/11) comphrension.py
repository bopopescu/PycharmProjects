# comprehension 1)list 2)tuple 3)dictionary  21/05/2018

# comprehension list
'''def sqr(l1):
    temp = []
    for i in l1:
        temp.append(i * i)
        #print(temp)
    print(temp)
listdata = [1,2,3,4,5]
sqr(listdata)

data = [i * i for i in listdata]
print(list(data))'''

'''def sqr(l1):
    temp = []
    for i in l1:
        if i % 2 == 0:
            temp.append(i * i)
        #print(temp)
    print(temp)
listdata = [1,2,3,4,5]
sqr(listdata)

data = [i * i for i in listdata if i % 2 == 0]
print(list(data))'''

# multiple for loop

'''def sqr(l1):
    temp = []
    for i in l1:
        if i % 2 == 0:
            temp.append(i * i)
        #print(temp)
    print(temp)
listdata = [1,2,3,4,5]
l2 = [10,20]
sqr(listdata)

#data = [i * i for i in listdata for j in l2] # to print l2
#data = [i * i for i in listdata for j in l2 if i % 2 == 0] # to check even no

# comprehension tuple 

#data = tuple(i * i for i in listdata for j in l2 )

# comprehension dictionary

#data = {i: i * i for i in listdata} 
# print(data)

#print(list(data))'''

# l1 = [1,2,3,4]
# print(dict(l1))

# using enumerate - divide index and assign values to it
'''l2 = [1,2,3,4]
temp = enumerate(l2)
print(list(temp))'''

'''l2 = [1,2,3,4]
temp = enumerate(l2)
#print(list(temp))
#print(temp)
for i,v in enumerate(l2):
    print(str(i) + '=>' + str(v))'''

'''l1 = ['a', 'b', 'c', 'd']
temp = enumerate(l1)
print(dict(list(temp)))'''

