#Given an unsorted array of numbers, find the 'K' largest numbers in it.
'''Solution1
def TopKNumbers(array,k):
    heap=[]
    for i in array:
        if len(heap)>=k:
            if i<=heap[-1]:
                continue
            else:
                heap.pop()
        heap.append(i)

        for j in range(len(heap)-1,0,-1):
            if heap[j]>heap[j-1]:
                swap(heap,j,j-1)
            else:
                break
    return heap

def swap(heap,i,j):
    temp=heap[i]
    heap[i]=heap[j]
    heap[j]=temp
'''
#Solution2-Educative
from heapq import *
def TopKNumbers(array,k):
    minheap=[]
    for i in range(k):
        heappush(minheap,array[i])
    
    for i in range(k,len(array)):
        if array[i]>minheap[0]:
            heappop(minheap)
            heappush(minheap,array[i])
    return minheap


def main():
    print(TopKNumbers([1,5,23,76,27,4,12,6],3))
    print(TopKNumbers([3,4,67,2],4))
    print(TopKNumbers([3,3,3,3],3))

main()