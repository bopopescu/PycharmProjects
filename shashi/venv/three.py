# list

'''l = []
print(l)'''

'''l = [1,2,'abc',11.12]
l[0] = [100]
print(l)'''

'''l = [1,2,'abc',11.12,'def']
print(l)
print(l[0])
print(l[:])
print(l[:2])
print(l[2:])
print(l[1:4])
print(l[2:2])
print(l[1:2])
print(l[1:-2])
print(l(-2:-4
print(l[-1:-3])
print(l *2 )'''

'''l2 = [1,2,3,4,5]

print(l2[-3:-1])
print(l2[-2:-4] # not correct syntax
'''

# append add one element in a list
'''l = [1,2,'abc',11.12]
l.append(300) 
l.append(400)
print(l)'''

# extend adding more elements in a list
'''l = [1,2,'abc',11.12]
l.extend([1000,2000,3000]) 
print(l)'''

# insert 4000 after 2 in a list
'''l = [1,2,'abc',11.12]
l.insert(2,4000)
print(l)'''

# pop remove abc  from index 2
'''l = [1,22,'abc',11.12]
l.pop(2) # remove index 
print(l)'''

# remove 255 from list
'''l = [125,255,'abc',11.12]
l.remove(255) # remove value
print(l)'''

# clear all the lists
'''l = [125,255,'abc',11.12]
l.clear() 
print(l)'''

# delete() del statement can be used to delete an element from the list. delete all items from startIndex to endIndex.
'''l = [125,255,'abc',11.12]
del l[0] 
print(l)'''

# reverse the lists
'''l = [1,2,0,-1,6,3,5,4]
l.reverse()
print(l)'''

# sort the lists in ascending order
'''l = [1,2,0,-1,6,3,5,4]
l.sort()
print(l)'''

# sort in descending order
'''l = [1,2,0,-1,6,3,5,4]
l.sort(reverse=True)
print(l)'''

# sort in ascending order
'''l = [1,2,0,-1,6,3,5,4]
l.sort(reverse=False)
print(l)'''


# count the 33 how many times repaeated
'''l = [1,33,0,5,6,33,5,4]
print(l.count(33))'''

# count the 5 how many times repaeated
'''l = [1,33,0,-5,6,33,5,4]
print(l.count(5))
print(l.count(10)) # returns 0 because 10 is not in the list
'''

# index 'abc' is in  which index position & 22 is in which index position
'''l = [1,22,'abc',11.12,55]
print(l.index('abc'))
print(l.index(22))'''

# copy of one list to another list
'''list1 = [1,22,'abc',11.12,55]
list2 = list1.copy()
list2.append(45)
print(list1)
print(list2)'''

# length of total list items
'''l = [1,22,'abc',11.12,55]
print(len(l))'''


