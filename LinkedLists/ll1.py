from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None





def llDupDel(linkedlist: LinkedList) -> LinkedList:

    temp = linkedlist.head


    newDict = {}
    while(temp != None):
        if(temp.value not in newDict):
            newDict[temp.value] = 1
        else:
            if(temp == linkedlist.head):
                linkedlist.head = linkedlist.head.next

            elif(temp.next == None):
                temp1 = linkedlist.head

                while(temp1.next.next != None):
                    temp1 = temp1.next
                temp1.next = None

            else:
                temp1 = linkedlist.head

                while(temp1.next.value != temp.value):
                    temp1 = temp1.next

                temp1.next = temp1.next.next






        temp = temp.next




    return linkedlist



def llInsertion(linkedlist:LinkedList, vals: List[int]) -> LinkedList:


    temp = linkedlist.head = Node(vals[0])

    for val in vals[1:]:

        temp.next = Node(val)
        temp = temp.next


    return linkedlist




def llPrint(linkedlist:LinkedList)-> None:

    temp = linkedlist.head

    while(temp != None):
        print(temp.value, end = ' ')



        temp = temp.next
    print("")






llist = LinkedList()


llist.head = Node(1)

e2 = Node(2)
e3 = Node(3)

llist.head.next = e2

e2.next = e3


llisttest = LinkedList()
vals = [1, 1, 3, 1,5]

llInsertion(llisttest, vals)

llPrint(llisttest)

llDupDel(llisttest)

llPrint(llisttest)


