def rotSubstringCheck(string1: str, string2:str) -> int:

    startingChar = string1[0]




    shifts = []


    i = 0
    for char in string2:
        if(char == startingChar):
            shifts.append(i)

        i+=1

    newstr = string


    for shift in shifts:
        newstr = rotateString(string2, shift)

        if newstr == string1:
            print("String is rotation substring")
            return 0



    print("String is not rotation substring")

    return 1



def rotateString(string:str , rot:int) -> str:

    rot = rot%len(string)

    newEnd = string[:rot]
    newStart = string[rot:]

    newStr = newStart+newEnd



    return newStr



string = "abcdefg"

string1 = "bcdefga"


string2 = "aaaaaaa"

rotSubstringCheck(string, string1)

rotSubstringCheck(string, string2)
