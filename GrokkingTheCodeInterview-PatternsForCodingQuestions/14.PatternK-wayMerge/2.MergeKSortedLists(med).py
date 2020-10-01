#Given an array of 'K' sorted LinkedLists, merge them into one sorted list.

from heapq import *
class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
#Solution2-Educative
    def __lt__(self,other):
        return self.val<other.val

def MergeKSortedLists(array):
    minheap=[]
    for root in array:
        if root:
            heappush(minheap,root)
    resulthead,resulttail=None,None
    while minheap:
        node=heappop(minheap)
        if not resulthead:
            resulthead=resulttail=node
        else:
            resulttail.next=node
            resulttail=resulttail.next
        if node.next:
            heappush(minheap,node.next)
    return resulthead

'''Solution1
def MergeKSortedLists(array):
    minheap=[]
    head=result=None
    for i in range(len(array)):
        heappush(minheap,(array[i].val,i))
        array[i]=array[i].next
    while minheap:
        num,index=heappop(minheap)
        node=ListNode(num)
        if not head:
            head=result=node
        else:
            result.next=node
            result=result.next
        if array[index]:
            heappush(minheap,(array[index].val,index))
            array[index]=array[index].next
    return head
'''

def main():
    l1=ListNode(2)
    l1.next=ListNode(4)
    l1.next.next=ListNode(6)

    l2=ListNode(3)
    l2.next=ListNode(5)
    l2.next.next=ListNode(7)

    l3=ListNode(1)
    l3.next=ListNode(6)
    l3.next.next=ListNode(8)

    result=MergeKSortedLists([l1,l2,l3])
    while result:
        print(str(result.val)+'>',end='')
        result=result.next

main()
    
    

