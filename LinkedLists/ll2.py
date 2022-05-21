from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def getnthVal(self, n):


        len = 0
        temp = self.head

        while(temp != None):
            len +=1

            temp = temp.next


        if(len< n):
            return None

        i = 0


        temp = self.head



        while(temp != None):
            i+=1

            if(i == n):
                return temp.value
            temp = temp.next


def llPrint(linkedlist: LinkedList) -> None:

    temp = linkedlist.head

    while(temp != None):
        print(temp.value, end=' ')

        temp = temp.next
    print("")





def nthLLVal(linkedlist: LinkedList, n: int) -> int:
    return 0


def llInsertion(linkedlist: LinkedList, vals: List[int]) -> LinkedList:

    temp = linkedlist.head = Node(vals[0])

    for val in vals[1:]:

        temp.next = Node(val)
        temp = temp.next

    return linkedlist
llisttest = LinkedList()
vals = [1, 1, 3, 1,5]
llInsertion(llisttest, vals)


print("Linked-list:")

llPrint(llisttest)


print("Nth value is:", llisttest.getnthVal(3))


