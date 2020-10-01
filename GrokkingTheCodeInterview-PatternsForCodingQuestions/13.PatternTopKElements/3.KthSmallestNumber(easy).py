#Given an unsorted array of numbers, find Kth smallest number in it.
#Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.
from heapq import *
def KthSmallestNumber(array,k):
    maxheap=[]
    for i in range(k):
        heappush(maxheap,-array[i])
    
    for i in range(k,len(array)):
        if array[i]<-maxheap[0]:
            heappop(maxheap)
            heappush(maxheap,-array[i])
    
    return -maxheap[0]

def main():
    print(KthSmallestNumber([1,5,23,76,27,4,12,6],3))
    print(KthSmallestNumber([3,4,67,2],4))
    print(KthSmallestNumber([3,3,3,3],3))

main()