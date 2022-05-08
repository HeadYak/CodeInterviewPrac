
from typing import List

def reverseStringPythonic(string: str) -> str:

    newstring = string[::-1]

    return newstring


def reverseStringC(chars: List[str]) -> List[str]:


    newList = []

    charsLen = len(chars)

    temp = 0

    while(temp < len(chars)-1):
        newList.append(chars[charsLen-2-temp])

        temp+=1

    return newList




string = "Hello World"

stringC = ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", None]

print(reverseStringPythonic(string))

print(reverseStringC(stringC))
