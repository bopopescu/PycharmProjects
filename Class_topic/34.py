# regular expression

# match : matches only one and return one value

# import re
#
# pattern = r'[a-z]+ \d+'
# string = "hi are I hello 33 something 4"
#
# obj = re.match(pattern,string)
# print(obj)




# +   1 or more value
#
# import re
#
# pattern = r'[a-z]+ \d+'
# string = "hi I hello 33 something 4"
#
# obj = re.match(pattern,string)
#
# if obj:
#     print(obj.group())
# else:
#     print("no match found")



# ?
#
# import re
#
# #pattern = r'[a-z]+ \d?'
# pattern = r'[a-z]+'
#
# string = "1hi I hello 33 something 4"
#
# obj = re.match(pattern,string)
#
# if obj:
#     print(obj.group())
# else:
#     print("no match found")



# * like \d*
#
# import re
#
# pattern = r'[a-z]+ \d*'
# string = "hi 66 I hello 33 something 4"
#
# obj = re.match(pattern,string)
#
# if obj:
#     print(obj.group())
# else:
#     print("no match found")



# d{2} 0r d{1,}
#
# import re
# #pattern = r'[a-z]+ \d{2}'
# #pattern = r'[a-z]+ \d{1,}'
# #pattern = r'[a-z]+ \d{0}'
# pattern = r'[a-z]+ \d{1}'
# string = "hi 678 I hello 33 something 4"
#
# obj = re.match(pattern,string)
#
# if obj:
#     print(obj.group())
# else:
#     print("no match found")



# # d{2,4}

# import re
#
# pattern = r'[a-z]+ \d{2,4}'
# string = "hi 123456 I hello 33 something 4"
#
# obj = re.match(pattern,string)
#
# if obj:
#     print(obj.group())
# else:
#     print("no match found")
#


# search

# import re
#
# #pattern = r'[a-z]+ \d+'
# pattern = r'\d+ [a-z]+'
#
# string = "hi hello @ 66 I something 4 jj"
#
# obj = re.search(pattern,string)
#
# if obj:
#     print(obj.group())
# else:
#     print("no match found")

