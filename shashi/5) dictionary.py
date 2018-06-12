# dictionary 11/05/2018

'''d1 = {
    'name': 'raju',
    'email': 'raju@gmail.com',
    'city': 'Bangalore',
    'phone': '123456',
    'salary': '11110.11'
}
'''

#print(d1)
#print(d1['name'])

# update
'''d1.update({'address': 'BTM'})
print(d1)
d1.update({'pincode': '5600078', 'age':27})
print(d1)'''

'''d1['xyz'] = 'abc' # without update function we can add item
print(d1)'''

# pop & popitem
'''d1.popitem() # delete last dictionary values by default - salary
print(d1)
d1.pop('name') # delete 'name' in dictionary
print(d1)'''

'''del d1['name'] # without pop function we can delete item
print(d1)'''

# get
'''print(d1['name'])
print(d1.get('email'))'''

# keys
'''temp = d1.keys()
print(temp)'''

# values
'''temp = d1.values()
print(temp)
print(list(temp)) # to print in list format
'''

# copy
'''d2 = d1.copy()
d1.update({'200':'200'})
print(d1)
print(d2)'''

'''for k in d1: # prints only keys
    print(k)'''

'''for v in d1: # it does not print  values
    print(v)'''


'''for k in d1: # print only values
    print(d1[k])'''

# items
'''for k,v in d1.items():
    print(k+ ":" +v)
print(list(d1.items()))
print(tuple(d1.items()))
print(str(d1.items()))
print(dict(d1))
print(dict(d1.items()))'''

# examples
'''l1 =[11,12,33,44]
l1.append({'name':"raju",'email':'rahu@gmail.com'}) # adding for multiple element
print(l1)

l1[4].update({'city':'bangalore'}) # update for single element
print(l1)

l1.append([100,200])
print(l1)

l1[5].append(400)
print(l1)

l1[5].append(500)
print(l1[5])

l1.append((1000,2000))
print(l1)

print(l1[6])

print(l1[6][0])
print(l1[6][1])
print(l1[6][2]) # does not print no value beacause it does not any item
'''

# In dictionary we can print list, tuple,dictionary(key:value pair ) 14/05/2018
'''l1 = [1,2,3,4]
d1 = {
    'l1':l1,
    't1':(1,2,3),
    'd2':{'a':1,'b':2,'c':3}
}
print(d1)
print(d1['d2']['a'])
print(d1['l1'][1])
print(d1['t1'][0])'''


'''m1 = [1,2,3,4]
d1 = {'a': 1, 'b': 2}

t1 =(m1,d1,1000)

t1[0].append(5) # m1 =(1,2,3,4)
print(t1)
t1[1].update({'c':3})
print(t1)'''



