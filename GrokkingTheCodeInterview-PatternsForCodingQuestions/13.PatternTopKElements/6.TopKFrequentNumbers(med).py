#Given an unsorted array of numbers, find the top 'K' frequently occurring numbers in it.
from heapq import *
def TopKFreqNum(nums,k):
    NumFreq={}
    for i in nums:
        if i not in NumFreq:
            NumFreq[i]=1
        else:
            NumFreq[i]+=1
    
    minHeap=[]

    for num, freq in NumFreq.items():
        heappush(minHeap,(freq,num)) #the order relys on the first item, which is 'freq' here.
        if len(minHeap)>k:
            heappop(minHeap)
    
    results=[]
    while minHeap:
        results.append(heappop(minHeap)[1])
    
    return results

def main():
    print(TopKFreqNum([2,4,6,7,9,8,4,2,7,4,2,9,4],3))

main()

