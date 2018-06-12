'''try:
    int("sds")
    print(name)
    name = "aaaa"
    open('dddddd')
    import asdfg
    print("went good...")

except (NameError, ValueError, ImportError):
    print("something went Wrong")

except NameError:
    print("NameError")

#except:
except ValueError:
    print("exception")

except ImportError:
    print("Importerror")

finally:
    print("i am always here.....")'''

# try example

'''try:
    num = input("number?")
    num = int(num)
    if num < 0:
        raise ValueError

except (NameError, ImportError):
    print("something went wrong")

except ValueError:
    print("Number can't be negative")

finally:
    print("i am always here")'''

# to enter a no
'''
while True:

    try:
        i = int(input("please enter a no"))
        break

    except ValueError:
        print("please enter a correct no ")
'''
