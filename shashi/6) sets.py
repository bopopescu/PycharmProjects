# sets

'''s1 = {1,2,3,4,1,3,3,4,5}
l1 = [1,2,3,1,3,2,4,5]
l1 = set(l1)
print(l1)
l1 = list(l1)
print(l1)
print(s1)'''

#s1 = {1,2,3,'xyz',12.11,55}
#print(s1)

# add
'''s1.add('abc')
print(t)
s1.add(100)
print(s1)
s1.add(1)
print(s1)'''

# update ( set object does not support indexing ,so update elements are not arranged  in order )
'''s1.update([111,222,333])
print(s1)
s1.update([1000])
print(s1)
s1.update([2000])
print(s1)
s1.update([3000])
print(s1)'''

# pop - by default it will remove first element in set
'''s1.pop()
print(s1)'''

# remove - particular element from sets and next time the element will not be visible in set
'''s1.remove(2)
print(s1)

# discard - if we want to discard
s1.discard(3)
print(s1)

# clear
s1.clear()
print(s1)'''

# intersection
# s1 = {1,2,3,4,5,1}
# s2 = {2,3,6,7}
# print(s1)
# print(s2)

# intersection
'''temp = s1.intersection(s2)
print(temp)
print("=============")

# intersection_upddate
s1.intersection_update(s2)
print(s1)
print(s2)'''

# union
'''temp = s1.union(s2)
print(temp)

# issubset - common element in both the sets
m1 = {1,2,3,4,5}
m2 = {2,3}
temp1 = m2.issubset(m1)
print(temp1)'''
