# decorator function
#
# def email(funName): # email - decorator : starting function name
#
#     def executeDeco():
#
#         print("i am in email decorator")
#         funName()
#
#     return executeDeco
#
# def name():
#     print("Raj")
#
# name()



# @email
#
# def email(funName): # email - decorator : starting function name , decorator means reusability
#
#     def executeDeco():
#
#         print("i am in email decorator")
#         funName()
#
#     return executeDeco
#
# @email
# def name():
#     print("Raj")
#
# name()



# comment funName - it only prints "i am in email decorator"

def email(funName): # email - decorator : starting function name , decorator means reusability

    def executeDeco():

        print("i am in email decorator")
        #funName()

    return executeDeco

@email
def name():
    print("Raj")

name()