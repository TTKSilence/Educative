#Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
#The algorithm should use constant space and the input LinkedList should be in the original form once the 
#algorithm is finished. The time complexity should be O(N).
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

def palindrome(head):
    slow,fast=head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

    secondhalf=reverse(slow)
    copy=secondhalf

    while secondhalf and head:
        if secondhalf.value!=head.value:
            break
        secondhalf=secondhalf.next
        head=head.next
    reverse(copy)
    if not secondhalf or not head:
        return True
    return False

def reverse(head):
    pre=None
    cur=head
    while cur:
        nex=cur.next
        cur.next=pre
        pre=cur
        cur=nex
    return pre

def main():
    head=Node(2)
    head.next=Node(4)
    head.next.next=Node(6)
    head.next.next.next=Node(6)
    head.next.next.next.next=Node(6)
    head.next.next.next.next.next=Node(4)
    print(palindrome(head))

    head.next.next.next.next.next.next=Node(2)
    print(palindrome(head))

main()