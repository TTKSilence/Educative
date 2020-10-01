#Given the head of a Singly LinkedList, 
#write a function to determine if the LinkedList has a cycle in it or not.

class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

def solution(head):
    fast=head
    slow=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            return True
    return False

def main():
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)
    head.next.next.next.next.next=Node(6)
    head.next.next.next.next.next.next=Node(7)
    print(str(solution(head)))

    head.next.next.next.next.next.next.next=head.next.next
    print(str(solution(head)))

    head.next.next.next.next.next.next.next=head.next.next.next
    print(str(solution(head)))

main()



