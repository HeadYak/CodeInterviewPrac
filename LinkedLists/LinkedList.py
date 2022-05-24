class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head

        while(temp != None):
            print(temp.value, end=' ')

            temp = temp.next
        print("")

    def insertionListVals(self, vals):
        if(len(vals) == 0):
            return

        temp = self.head = Node(vals[0])

        for val in vals[1:]:
            temp.next = Node(val)
            temp = temp.next

    #For linked-lists with even number of values, function returns node that is right of the middle
    def getMiddleNode(self):
        slow = self.head
        fast = self.head

        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow
    def appendLinkedList(self,node):
        if(self.head== None):
            self.head = node

            return
        temp = self.head
        while(temp.next!=None):
            temp = temp.next

        temp.next = node

        return



