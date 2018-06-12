#To open a text file, write

'''fh = open("hello.txt", "w")
fh.write('football\n')#write() takes exactly one argument
fh.write("************************")
fh.writelines(['hello\n','hi\n', 'write file operations\n'])
print(fh.writable()) # True or False
print(fh) # <_io.TextIOWrapper name='Hello.txt' mode='w' encoding='cp1252'
fh.close()'''

# read

'''file = open("hello.txt", "r")
print(file.readable()) # True or False

data = file.read()
data = file.readline()
data = file.readlines()
print(data)
file.close()
print(fh) # <_io.TextIOWrapper name='Hello.txt' mode='r' encoding='cp1252' '''

# To append to file:

'''fh = open("Hello.txt", "a")
fh.write("Hello World again")
fh.writelines(['\nShashi','\nshiva\n', 'Harsha\n'])
fh.close
print(fh) # <_io.TextIOWrapper name='Hello.txt' mode='a' encoding='cp1252' '''

# with open one file

'''with open('Hello.txt')as file5:
    print(file5.read())'''

# with open two file

'''with open('Hello.txt')as file5,open('test.py')as file6:
    print(file5.read())
    print(file6.read())'''


# convert one file content into uppercase and display the output to another file

m1 = open("Demo", "w")
m1.write("hello Hi hai")
m1.close()
data = "";

with open("Demo")as m2:
    m2 = m2.read()
    data = m2.upper()
#print(data) # to display here

m3 = open("Dummy", "w") # to display output in Dummy file
m3.write(data)
m3.close()

'''# convert one file content count the no of repeated occurrence words output to another file

#l1 = 'hi hello hi'
string = 'hi how are you hi'

file1 = open("hello.txt", "w")
#file1.write(l1)
file1.write(string)
file1.close()

d1 = {}
data = string.split(" ")

with open("hello.txt")as file2:
    file2 = file2.read()
    for word in data:
        d1[word] = data.count(word)
    print(d1)

# another method
file3 = open("Dummy.txt","w")
file3 = file3.write(str(d1))'''


