# #{3} after . match com
# import re
#
# pattern = r'[^@]+@[^@]+\.[^@]{3}'
# string = "xyz@gmail.com abc@gmail.com raj@gmail.com dd"
#
# obj = re.findall(pattern,string)
#
# if obj:
#     print(obj)
# else:
#     print("no match found")



# r'[^@ ] - remove spaces , after raj@ma manas@gmail.com

# import re
#
# pattern = r'[^@ ]+@[^@]+\.[^@]{3}'
# string = "xyz@gmail.com abc@gmail.com raj@gma manas@gmail.com dd"
#
# obj = re.findall(pattern,string)
#
# if obj:
#     print(obj)
# else:
#     print("no match found")



# compile
# to print email format - pattern = r'[^@]+@[^@]+\.[^@]{3}'
#
# import re
#
# pattern = r'[^@ ]+@[^@]+\.[^@]{3}'
# com = re.compile(pattern)
# string = "xyz@gmail.com abc@gmail.com raj@gma manas@gmail.com dd"
#
# obj = com.findall(string)  # remove pattern
#
# if obj:
#     print(obj)
# else:
#     print("no match found")