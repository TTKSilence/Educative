#Given the head of a LinkedList and two positions 'p' and 'q',
#reverse the LinkedList from position 'p' to 'q'.

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

def ReverseSub(head,p,q):
    if p==q:
        return head
    pre,cur,nex=None,head,None
    while cur.value!=p:
        pre=cur
        cur=cur.next
    #save the address of the junction using pointers
    firstnode=pre
    lastnode=cur
    #reverse the middle part
    while pre.value!=q:
        nex=cur.next
        cur.next=pre
        pre=cur
        cur=nex
    #connect these three parts
    if firstnode is not None:
        firstnode.next=pre
    else:
        head=pre
    lastnode.next=cur

    return head

def main():
    head=Node(2)
    head.next=Node(4)
    head.next.next=Node(6)
    head.next.next.next=Node(8)
    head.next.next.next.next=Node(10)
    ReverseSub(head,4,8).print_list()

main()
    

