#Given the head of a Singly LinkedList that contains a cycle,
#write a function to find the starting node of the cycle.

class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

    def print_list(self):
        temp=self
        while temp is not None:
            print(temp.value,end='')
            temp=temp.next
        print()
    
def find_cycle_start(head):
    #move the pointers into the cycle
    fast,slow=head.next,head
    while fast!=slow:
        fast=fast.next.next
        slow=slow.next
    #count the cyclelength
    cur=slow.next
    cyclelength=1
    while cur!=slow:
        cur=cur.next
        cyclelength+=1
    #let the fast pointer move ahead 'cyclelength' moves alone
    fast,slow=head,head
    for _ in range(cyclelength):
        fast=fast.next
    #let both pointers move synchronous/simultaneous
    while fast!=slow:
        fast=fast.next
        slow=slow.next
    return slow

def main():
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)
    head.next.next.next.next.next=Node(6)
    head.next.next.next.next.next.next=Node(7)

    head.next.next.next.next.next.next.next=head.next.next
    print("The cycle start:" + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next.next=head.next
    print("The cycle start:" + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next.next=head.next.next.next
    print("The cycle start:" + str(find_cycle_start(head).value))

main()

