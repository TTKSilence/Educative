#Given the head of a Singly LinkedList, reverse the LinkedList.
#Write a function to return the new head of the reversed LinkedList
class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

    def print_list(self):
        temp=self
        while temp is not None:
            print(temp.value, end=" ")
            temp=temp.next
        print()

def Reverse(head):
    pre,cur,nex=None,head,None
    while cur:
        nex=cur.next # pointer 'nex' to save the next node's address
        cur.next=pre # reverse the 'cur' node
        pre=cur #move the pointer 'pre' backward ('cause its reversal order)
        cur=nex #move the pointer 'cur' forward
    return pre

def main():
    head=Node(2)
    head.next=Node(4)
    head.next.next=Node(6)
    head.next.next.next=Node(8)
    head.next.next.next.next=Node(10)
    Reverse(head).print_list()

main()
