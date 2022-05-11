from posixpath import split
from typing import List

def whitespaceReplace(string: List[str]) -> List[str]:

    if(set(string) == {' '}):
        return ["%20"]


    if(len(string) == 0):
        return string









    i = len(string)-1

    while(string[i] == ' '):
        string.pop(i)
        i = i-1



    i = 0

    maxLen = len(string)

    while(i < 17):
        if(string[i] == ' '):
            print(string)
            string[i] = "0"
            # string.insert(i, "0")
            string.insert(i, "2")
            string.insert(i, "%")
            i+=4

        else:
            i+=1



    return string










string = list("Mr John Smith")


whitespaceReplace(string)



