#Given 'M' sorted arrays, find the K'th smallest number among all the arrays.
from heapq import *

def KthSmallestNumber(array,k):
    minheap=[]
    for i in range(len(array)):
        heappush(minheap,(array[i][0],0,i))   
    count=0
    while minheap:
        num,index,nums_index=heappop(minheap)
        count+=1
        if count==k:
            break
        if index<len(array[nums_index])-1:
            heappush(minheap,(array[nums_index][index+1],index+1,nums_index))
    return num

def main():
    l1=[0,3,6,9]
    l2=[1,4,7,10]
    l3=[2,5,8,11]

    print(KthSmallestNumber([l1,l2,l3],6))

main()
    