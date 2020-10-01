#Given an array, find the sum of all numbers between the K1th and K2th smallest elements of that array.
from heapq import *
def SumOfElements(nums,k1,k2):
    '''Solution1
    maxheap=[]
    for i in range(k2-1):
        heappush(maxheap,-nums[i])
    for i in range(k2-1,len(nums)):
        heappush(maxheap,-nums[i])
        heappop(maxheap)
    sum=0
    for _ in range(k2-k1-1):
        sum-=heappop(maxheap)
    return sum
    '''
    #Solution2-Educative
    minheap=[]
    for i in range(len(nums)):
        heappush(minheap,nums[i])
    for _ in range(k1):
        heappop(minheap)
    sum=0
    for _ in range(k1,k2-1,1):
        sum+=heappop(minheap)
    return sum


def main():
    print(SumOfElements([1,3,12,5,15,11],3,6))
    print(SumOfElements([26,23,20,17,16,7,5,2],3,7))

main()