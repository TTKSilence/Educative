#Given the head of a LinkedList and a number 'k',
#reverse every alternating 'k' sized sub-list starting from the head.
#If in the end, you are left with a sub-list with less than 'k' elements, reverse it too.
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

def ReverseAK(head,k):
    pre,cur,nex=None,head,None
    alternating=True   #To judge if the alternating is needed in this iteration
    while cur:
        firstnode=pre
        lastnode=cur
        i=0
        if alternating:
            while i<k and cur:
                nex=cur.next
                cur.next=pre
                pre=cur
                cur=nex
                i+=1
            if firstnode:
                firstnode.next=pre
            else:
                head=pre
            lastnode.next=cur
            pre=lastnode
        else:
            while i<k and cur:
                pre=pre.next
                cur=cur.next
                i+=1
        alternating= not alternating
    return head

def main():
    head=Node(2)
    head.next=Node(4)
    head.next.next=Node(6)
    head.next.next.next=Node(8)
    head.next.next.next.next=Node(10)
    head.next.next.next.next.next=Node(12)
    head.next.next.next.next.next.next=Node(14)
    ReverseAK(head,3).print_list()

main()
        
