# File Operations 1) open() 2) read(), write(), append() 3)close()

# open , write
'''file = open('fileDemo', 'w')
file.write('hello, How you\n')
#file.close()
print(file)'''

# open, writeable, writelines
'''file = open('fileDemo', 'w')
file.writelines(['hello\n','hi\n', 'write file operations\n'])
print(file.writable())
file.close()'''

# open, readable
'''file = open('fileDemo', 'r')
print(file.readable())
file.close()'''

# open, writelines ,write
'''file = open('fileDemo', 'w')
file.writelines(['hello\n','hi\n', 'write file operstions\n'])
file.write('hello')
file.close()'''

# open
'''file = open('fileDemo')
print(file)
file.close()'''

'''file = open('fileDemo')
#data = file.read()
data = file.readline()
#data = file.readlines()
print(data)
file.close()'''

'''file = open('test.py')
#data = file.read()
data = file.readline()
#data = file.readlines()
print(data)
file.close()'''

# with open one file
'''with open('fileDemo')as file:
    print(file.read())'''

# with open two files
with open('fileDemo')as file, open('test.py')as file2:
    print(file.read())
    print(file2.read())

