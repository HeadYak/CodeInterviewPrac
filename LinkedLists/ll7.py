from LinkedList import LinkedList, Node


def palindromeCheck(linkedlist: LinkedList) -> bool:

    stack = []


    temp = linkedlist.head

    while(temp!= None):

        stack.append(temp.value)
        temp = temp.next


    temp = linkedlist.head


    while(temp!=None):
        if(temp.value != stack.pop()):
            return False

        temp = temp.next
    return True


linkedlist1 = LinkedList()
linkedlist2 = LinkedList()

vals1 = [1, 2, 3]

vals2 = [5, 5, 5]

linkedlist1.insertionListVals(vals1)

linkedlist2.insertionListVals(vals2)

print(palindromeCheck(linkedlist1))

print(palindromeCheck(linkedlist2))
