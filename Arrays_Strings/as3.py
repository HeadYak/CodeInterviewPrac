
def permCheck(string1:str, string2: str) -> bool:
    """
    Checks if two strings are permutations of each other
    Arguments:
        string1: a string
        string2: a string
    Return:
        True if strings are permutations of each other
        False if strings are not permutations of each other
    """

    sortedStr1 = sorted(string1)

    sortedStr1 = "".join(sortedStr1)


    sortedStr2 = sorted(string2)

    sortedStr2 = "".join(sortedStr2)


    if(sortedStr1 == sortedStr2):
        return True
    else:
        return False

#Question can also be completed through creating a hashmap of the frequencies of each character within each string before comparing the frequencies to determine
#if strings are permutations of each other



string1 = "Hello World"

string2 = "Bye World"

string3 = "World Hello"
print("Performing permCheck on \"%s\" and \"%s\"" %(string1,string2))

# help(permCheck)

if(permCheck(string1,string2)):
    print("Strings are permutations of each other")
else:
    print("Strings not permutations of each other")
print("\n")


print("Performing permCheck on \"%s\" and \"%s\"" % (string1, string1))

if(permCheck(string1, string1)):
    print("Strings are permutations of each other")
else:
    print("Strings not permutations of each other")
print("\n")


print("Performing permCheck on \"%s\" and \"%s\"" % (string1, string3))

if(permCheck(string1, string3)):
    print("Strings are permutations of each other")
else:
    print("Strings not permutations of each other")







