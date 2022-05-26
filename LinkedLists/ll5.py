from LinkedList import LinkedList


def LinkedListNumSumRev(linkedlist1, linkedlist2):
    val = 0


    temp = linkedlist1.head
    len1 = 0
    len2 = 0




    while(temp != None):
        len1 += 1
        temp = temp.next


    temp = linkedlist2.head

    while(temp != None):
        len2 += 1
        temp = temp.next

    temp1 = linkedlist1.head
    temp2 = linkedlist2.head

    counter = 0
    while(temp1 != None):

        val = val + temp1.value * 10 ** (len1-counter-1)

        counter = counter+1

        temp1 = temp1.next

    counter = 0
    while(temp2 != None):

        val = val + temp2.value * 10 ** (len2-counter-1)

        counter = counter+1

        temp2 = temp2.next



    return val



def LinkedListNumSum(linkedlist1, linkedlist2):
    temp1 = linkedlist1.head
    temp2 = linkedlist2.head


    counter = 0

    val = 0

    while(temp1 != None):

        val = val + temp1.value * 10 ** counter


        counter = counter+1

        temp1 = temp1.next


    counter = 0
    while(temp2 != None):
        val = val + temp2.value *10 **counter
        counter = counter +1

        temp2 = temp2.next

    return val



linkedlist1 = LinkedList()
linkedlist2 = LinkedList()

vals1 = [1,2,3]

vals2 = [5,5,5]

linkedlist1.insertionListVals(vals1)
linkedlist2.insertionListVals(vals2)

res = LinkedListNumSum(linkedlist1,linkedlist2)
res1 = LinkedListNumSumRev(linkedlist1, linkedlist2)
print(res)
print(res1)


