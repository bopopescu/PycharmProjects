# json for dictionary

'''from json import dumps,loads

d1 = {'name':"Raj", 'email':'shashi@gmail.com'}
file = open("shashi","w")
file.write(dumps(d1))
file.close()

file1 = open("shashi")
content = file1.read()
d2 = loads(content)

print(d2['name'])
file1.close()'''

# json for list

from json import dumps,loads

m1 = [1,2,3,4]

s1 = open("sharath","w")
s1.write(dumps(m1))
s1.close()

file = open("sharath")
content = file.read()
content = loads(content)

#for i,v in enumerate(content): # other method using enumerate
 #   content[i] = v * v

for i in range(0,len(content)):
   content[i] = content[i] * content[i]
print(content)

#for i in (len(content)): # TypeError: 'int' object is not iterable - for loop it should in range so
    #content[i] = content[i] * content[i]

file = open('sqr_result','w')
file.write(dumps(content))
file.close()