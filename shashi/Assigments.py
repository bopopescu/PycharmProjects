# Assigment : how to remove list with in list

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

# Assigment : how to count repeated string in a given sting

string = 'hi how are you'
data = string.split(" ")
d1 = {}
for word in data:
    d1[word] = data.count(word)
print(d1)

# count the no of occurrence in a list

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

