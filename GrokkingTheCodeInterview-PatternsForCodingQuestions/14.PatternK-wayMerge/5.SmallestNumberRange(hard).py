#Given 'M' sorted arrays,
#find the smallest range that includes at least one number from each of the 'M' lists.
from heapq import *
def SmallestNumberRange(array):
    minheap=[]
    maxnum=-float('inf')
    result=[]
    for i in range(len(array)):
            heappush(minheap,(array[i][0],0,i))
            maxnum=max(maxnum,array[i][0])
    '''Solution1
    rang=float('inf')
    while minheap:
        num,index,list=heappop(minheap)
        if maxnum-num<rang:
            rang=maxnum-num
            result=[num,maxnum]
        if index<len(array[list])-1:    
            heappush(minheap,(array[list][index+1],index+1,list))
            maxnum=max(maxnum,array[list][index+1])
        else:
            break
    '''
    #Solution2-Educative
    rangeend,rangestart=float('inf'),0
    while len(minheap)==len(array):
        num,index,list=heappop(minheap)
        if maxnum-num<rangeend-rangestart:
            rangestart=num
            rangeend=maxnum
        if len(array[list])>index+1:
            heappush(minheap,(array[list][index+1],index+1,list))
            maxnum=max(maxnum,array[list][index+1])

    return [rangestart,rangeend]

def main():
    print(SmallestNumberRange([[2,7,10,13],[9,10,12,15],[5,16,18,20]]))

main()

        

