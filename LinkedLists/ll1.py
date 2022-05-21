from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def sortedMerge(self,a,b):
        result = None

        # Base cases
        if a == None:
            return b
        if b == None:
            return a

        # pick either a or b and recur..
        if a.value <= b.value:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result

    def mergeSort(self, head):
        if head == None or head.next == None:
            return head

        middle = self.getllMiddle(head)

        middleNext = middle.next

        middle.next = None

        left = self.mergeSort(head)

        right = self.mergeSort(middleNext)


        sortedll = self.sortedMerge(left, right)

        return sortedll

    def getllMiddle(self,head):
        if(head == None):
            return head
        slow = head
        fast = head

        while(fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow





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


def llDupDelNoBuffer(linkedlist: LinkedList) -> LinkedList:
    linkedlist.head = linkedlist.mergeSort(linkedlist.head)



    temp = linkedlist.head

    while(temp.next != None):
        if(temp.value == temp.next.value):
            if(temp == linkedlist.head):
                linkedlist.head = linkedlist.head.next
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
print("Removal of duplicates using buffer:")

print("Linked-list:")
llPrint(llisttest)
llDupDel(llisttest)
print("After removal of duplicates")
llPrint(llisttest)
print("")


llisttest1 = LinkedList()
vals = [1, 3,5, 2, 4, 3,1]
llInsertion(llisttest1, vals)
print("Removal of duplicates through merge sorting")
print("Linked-list:")
llPrint(llisttest1)

print("Linked-list after merge sorting")
llisttest1.head = llisttest1.mergeSort(llisttest1.head)
llPrint(llisttest1)
llDupDel(llisttest1)
print("After removal of duplicates")
llPrint(llisttest1)
# llDupDelNoBuffer(llisttest1)

