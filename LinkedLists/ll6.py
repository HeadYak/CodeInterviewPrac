from LinkedList import LinkedList, Node

### This is too hard to do in Python without object addresses


def loopCheck(linkedlist: LinkedList) -> Node:

    nodeDict = {}



    temp = linkedlist.head


    while(temp!=None):

        if temp not in nodeDict:
            nodeDict[temp] = 1

        else:
            return temp.value



        temp = temp.next





    return 0




linkedlist1 = LinkedList()
linkedlist2 = LinkedList()

vals1 = [1, 2, 3]


linkedlist1.insertionListVals(vals1)

temp = linkedlist1.head


while(temp != None):
    temp = temp.next

