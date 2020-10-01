#Given an array of numbers and a number 'K',
#we need to remove 'K' numbers from the array such that we are left with maximum distinct numbers.
from collections import Counter
from heapq import *
def MaxDistElem(nums,k):
    '''Solution1
    numcount=Counter(nums)
    distnum=0
    minheap=[]
    for i in numcount:
        if numcount[i]==1:
            distnum+=1
        else:
            heappush(minheap,(numcount[i],i))
    j=0
    while j<k and minheap:
        temp=heappop(minheap)
        j+=temp[0]-1
        if j<=k:
            distnum+=1
    if j<k:
        distnum-=k-j
    return max(0,distnum)
    '''
    #Solution2-Educative
    distnum=0
    if len(nums)<=k:
        return distnum
    numcount=Counter(nums)
    minheap=[]
    for i in numcount:
        if numcount[i]==1:
            distnum+=1
        else:
            heappush(minheap,(numcount[i],i))
    while k>0 and minheap:
        temp=heappop(minheap)
        k-=temp[0]-1
        if k>=0:
            distnum+=1
    if k>0:
        distnum-=k
    return distnum
        

    

def main():
    print(MaxDistElem([7,7,3,5,8,5,3,3],3))
    print(MaxDistElem([3,5,11,12,11,12],3))
    print(MaxDistElem([1,2,3,3,3,3,3,4,4,5,5,5],3))
    print(MaxDistElem([1,2,3,3,3,3,3,4,4,5,5,5],4))

main()
    