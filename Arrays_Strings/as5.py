

def genFreqString(string: str) -> str:

    newStr = ""

    currChar = string[0]

    counter = 0

    for char in string:
        if(char == currChar):
            counter+=1
        else:
            newStr  = newStr + currChar + str(counter)

            currChar = char
            counter = 1

    newStr = newStr + currChar + str(counter)

    if(len(newStr) >= len(string)):
        return string


    return newStr





string = "aabcccccaaa"

res = genFreqString(string)

print(res)
