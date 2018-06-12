
# findall - don't use group it will catch error
#
# import re
#
# pattern = r'[a-z]+ \d+'
# string = "hi hello 66 I something 4"
#
# obj = re.findall(pattern,string)
#
# if obj:
#     print(obj)
# else:
#     print("no match found")



# finditer
#
# import re
#
# pattern = r'[a-z]+ \d+'
# string = "hi hello 66 I something 4 hey Dude"
#
# obj = re.finditer(pattern,string)
#
# if obj:
#     #print(obj)
#     for match in obj:
#         print(match.group())
# else:
#     print("no match found")



# split \s - based on symbols \s
#
# import re
#
# pattern = r'\s'
# string = "hi hello 66 I something 4 hey Dude"
#
# obj = re.split(pattern,string)
#
# if obj:
#     print(obj)
# else:
#     print("no match found")



# based on digits \d
#
# import re
#
# pattern = r'\d'
# string = "hi hello 66 I something 4 hey Dude"
#
# obj = re.split(pattern,string)
#
# if obj:
#     print(obj)
# else:
#     print("no match found")



# @

# import re
#
# pattern = r'@'
# string = "hi hello 66 I  @ something 4 hey Dude"
#
# obj = re.split(pattern,string)
#
# if obj:
#     print(obj)
# else:
#     print("no match found")