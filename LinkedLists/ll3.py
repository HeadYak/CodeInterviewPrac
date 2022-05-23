from LinkedList import LinkedList, Node


def delMiddleNode(node: Node) -> None:
    node.value = node.next.value

    node.next = node.next.next

linkedlist = LinkedList()


vals = [1,2,3,4,5,6]

linkedlist.insertionListVals(vals)
linkedlist.printLinkedList()

node = linkedlist.getMiddleNode()




delMiddleNode(node)



linkedlist.printLinkedList()
