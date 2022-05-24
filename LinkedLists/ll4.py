import copy
from pdb import line_prefix
from LinkedList import LinkedList, Node




def partitionLinkedList(linkedlist: LinkedList, partiVal: int) -> LinkedList:


    lesserLL = LinkedList()
    greaterLL = LinkedList()

    temp = linkedlist.head

    while(temp != None):

        print(temp.value)

        if(temp.value < partiVal):
            ## Look into why Node typecasting is needed for this to work
            lesserLL.appendLinkedList(Node(temp.value))

        else:
            greaterLL.appendLinkedList(Node(temp.value))


        temp = temp.next

    temp = lesserLL.head


    while(temp.next!= None):
        temp= temp.next
    temp.next = greaterLL.head




    lesserLL.printLinkedList()

    return linkedlist




linkedlist = LinkedList()
testlinkedlist = LinkedList()
vals= [100,500,1,4,5,11,7]


linkedlist.insertionListVals(vals)

linkedlist.printLinkedList()



partitionLinkedList(linkedlist, 10)

