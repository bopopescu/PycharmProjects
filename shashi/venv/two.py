# Types of Built-in String Methods : 09/05/2018

word = "Hello World"

#word.isalnum()  # check if all char are alphanumeric
#word.isalpha()  # check if all char in the string are alphabetic
#word.isdigit()  # test if string contains digits
#word.istitle()  # test if string contains title words
#word.isupper()  # test if string contains upper case
#word.islower()  # test if string contains lower case
#word.isspace()  # test if string contains spaces
#word.endswith('d')  # test if string endswith a d
#word.startswith('H')  # test if string startswith H
#word.replace('Hello', "Python") # test if Hello is replaced by Python
#word.find('l') # test if string l is  true it searches index position or -1 value if false
#word.count('o') # test if string  o repeats how many times
#word.index('W') # test if sring W in which indexing number


#print(word.isalnum())
#print(word.isalpha())
#print(word.isdigit())
#print(word.istitle())
#print(word.upper())
#print(word.isupper())
#print(word.lower())
#print(word.islower())
#print(word.isspace())
'''w1 = "\n \t \n"
print(w1.isspace())
w2 = "    "
w3 =''
print(w2.isspace())
print(w3.isspace())'''
#print(word.endswith('d'))
#print(word.startswith('H'))
#print(word.replace('Hello', "Python"))
#print(word.find('l'))
#print(word.count('o'))
#print(word.index('W'))


# Below are 3 methods to type Email Format
'''name = "Raju Rai"
email = "raju@gmail.com"
name = "Name:{0} \nEmail:{1}".format(name,email)
print(name)'''
#print(email[0])


'''name = "Raju Rai"
email = "raju@gmail.com"
name = "Name:%s \nEmail:%s" %(name,email)
print(name)'''


'''name = "Raju Rai"
email = "raju@gmail.com"
age = 27
name = "Name:" +name+ "\nEmail:" +email + "\nAge: "  +str(age)
print(name)'''


# Encode & Decode a string
'''name = "5555"
print(name.encode())'''
#print(name.decode())  #in this version decode has been removed


# To find len of the string
'''name = "555555"
name = len(name)
print(name)'''

# strip : Remove blank spaces
'''name = "0000000Raju Rai0000000"
name = name.strip('0')
print(name.strip('0'))'''

# lstrip : Remove blank spaces from left
'''name = "111111Raju Rai1111111"
name = name.lstrip('1')
print(name.lstrip('1')'''

# rstrip : Remove blank spaces from right
'''name = "**************Raju Rai****************"
name = name.rstrip('*')
print(name.rstrip('*'))'''


# split remove underscore from email
'''email = "hello_python_hello_djanjo"
print(email.split("_"))
print(email.split('h'))
e2 = "hello python hello djanjo"
print(e2.split(" "))'''

# split remove @ from email
'''email = "raju@gmail.com"
print(email.split('@'))'''

'''name="guru99 career"		
print(name.split('r'))'''


# Replace a string
'''name = "Sammy has a balloon"
print(name.replace('has',"had"))'''


# Reverse a string
'''name = "12345"
print(" ".join(reversed(name)))
print("".join(reversed(name)))'''

# Join a String
'''name = "hello python"
print(",".join(name))'''

'''s = "-";
seq = ("a","b","c")
print (s.join(seq))'''

# counting the no of words from the string 10/05/2018
'''a = "hi hello"
b = "Sha_shi_kum_ar"
print(b.split("_"))
print(a.split(" "))
print(a.split("o"))
print(a.split("h"))
print(len(a.split("e"))) # count the no of words "e" repeated including spaces
print(len(a)) # count the total no of leters'''


# counting the no of words from strip
'''a = "hi eat With"
#print(a.strip('hi')) # strip hi from begining and to  end
#print(a.strip('ht'))
print(a.strip('eat')) # does not strip because 'eat' is in center position
print(len(a))'''
