


def dupCheck(string):
    freqDict = {

    }
    for char in string:
        if(char not in freqDict):
            freqDict[char] = 1
        else:
            print("First duplicate detected: " + char)
            return

    print("All unique characters")
    return



def dupCheck_NoDS(string):
    sortedString = sorted(string)

    for i in range(len(sortedString)-1):
        if(sortedString[i] == sortedString[i+1]):
            print("First duplicate detected: " + sortedString[i+1])




string = "abcdd"

print("String: " + string +"\n")

print("Checking for duplicates using hashmap (Python dictionary)")
dupCheck(string)
print("\n")
print("Checking for duplicates through sorting")
dupCheck_NoDS(string)


