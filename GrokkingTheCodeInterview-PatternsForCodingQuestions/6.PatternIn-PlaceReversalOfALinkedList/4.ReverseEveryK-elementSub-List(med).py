#Given the head of a LinkedList and a number 'k',
#reverse every 'k' sized sub-list starting from the head.
#If, in the end, you are left with a sub-list with less than 'k' elements,reverse it too.

class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
    
    def print_list(self):
        temp=self
        while temp is not None:
            print(temp.value,end=" ")
            temp=temp.next
        print()

def ReverseK(head,k):
    pre,cur,nex=None,head,None
    
    while cur:
        #record the addresses between the junction
        firstnode=pre
        lastnode=cur
        i=0
        #reverse the sublist
        while i<k and cur:
            nex=cur.next # pointer 'nex' to save the next node's address
            cur.next=pre # reverse the 'cur' node
            pre=cur #move the pointer 'pre' backward ('cause its reversal order)
            cur=nex #move the pointer 'cur' forward
            i+=1
        #Move the pointers to the start of the next sublist
        if firstnode:
            firstnode.next=pre
        else:
            head=pre
        lastnode.next=cur
        #'cur' already points to the start of the next sublist, no need to move
        #move the pointer 'pre' so as to keep following 'cur'.
        pre=lastnode
    return head

def main():
    head=Node(2)
    head.next=Node(4)
    head.next.next=Node(6)
    head.next.next.next=Node(8)
    head.next.next.next.next=Node(10)
    ReverseK(head,2).print_list()

main()
