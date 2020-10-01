#Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.
#If the total number of nodes in the LinkedList is even, return the second middle node.

class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

    def print_list(self):
        temp=self
        while temp:
            print(temp.value,end='->')
            temp=temp.next
        print('None')

def solution(head):
    fast,slow=head,head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    return slow.value

def main():
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)
    print(solution(head))

    head.next.next.next.next.next=Node(6)
    print(solution(head))

    head.next.next.next.next.next.next=Node(7)
    print(solution(head))

    head.print_list()

main()

    