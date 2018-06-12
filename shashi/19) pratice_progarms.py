# pratice programs

# d = {'hello': 'world'}

# print(d.get('hello', 'default_value')) # prints 'world'
# print(d.get('thingy', 'default_value')) # prints 'default_value'
#
# print(d.items()) # prints ('hello', 'world')
# print(d.values()) # prints ['world']
# print(d.keys()) #['hello']


# # Or:
# if 'hello' in d:
#     print(d['hello'])


# # Filter elements greater than 4
# a = [3, 44, 15]
# b = []
# for i in a:
#     if i > 4:
#         b.append(i)
# print(b)

# a = [3, 4, 5]
# b = [i for i in a if i > 4]
# print(b)
#
# # Or:
# b = filter(lambda x: x > 4, a)
# print(list(b))

# Add three to all list members.
# a = [3, 4, 5]
# for i in range(len(a)):
#     a[i] = a[i] + 3
#     print(a[i])

# a = [3, 4, 5]
# a = [i + 3 for i in a]
# print(a)

## Or:
# a = map(lambda i: i + 3, a)
# print(list(a))

# to enter a no
'''
while True:

    try:
        i = int(input("please enter a no"))
        break

    except ValueError:
        print("please enter a correct no ")
'''
