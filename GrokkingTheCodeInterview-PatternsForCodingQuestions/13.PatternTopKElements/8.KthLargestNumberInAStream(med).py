#Design a class to efficiently find the Kth largest element in a stream of numbers.
#The class should have the following two things:
    #1. The constructor of the class should 
    #   accept an integer array containing initial numbers from the stream and an integer 'K'.
    #2. The class should expose a function add(int num) which will store the given number
    #   and return the Kth largest number.
from heapq import *
class KthLargestElement:
    '''Solution1
    def __init__(self,nums,k):
        self.nums=nums
        minheap=[]
        for i in range(k):
            heappush(minheap,nums[i])
        for i in range(k,len(nums)):
            if nums[i]>minheap[0]:
                heappop(minheap)
                heappush(minheap,nums[i])
        self.minheap=minheap
    
    def add(self,num):
        self.nums.append(num)
        if num>self.minheap[0]:
            heappop(self.minheap)
            heappush(self.minheap,num)
        return self.minheap[0]
    '''
    #Solution2-Educative
    def __init__(self,nums,k):
        self.nums=nums
        self.k=k
        self.minheap=[]
        for i in self.nums:
            self.add(i)  #Where is the returned value?
        
    def add(self,num):
        heappush(self.minheap,num)
        if len(self.minheap)>self.k:
            heappop(self.minheap)
        return self.minheap[0]


def main():
    input=[3,2,6,5,8,9]
    Problem=KthLargestElement(input,4)
    print(Problem.add(7))
    print(Problem.add(4))
    print(Problem.add(8))

main()
        
        