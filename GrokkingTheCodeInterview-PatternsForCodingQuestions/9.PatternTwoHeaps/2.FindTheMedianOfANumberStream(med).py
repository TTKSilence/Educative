#Design a class to calculate the median of a number stream.
#The class should have two methods like:
#   insertNum(int num): store the number in the class
#   findMedian(): return the median of all numbers inserted in the class
#If the count of numbers inserted in the class is even, the median will be the average of the middle two.
from heapq import *
class FindTheMedians:
    maxheap=[]
    minheap=[]
    def insertNum(self,num):
        # '-' is to let numbers from the maxheap can sort from large to small top-to-bottom
        #since it should be from small to large.
        if not self.maxheap or -self.maxheap[0]>=num: 
            heappush(self.maxheap,-num)
        else:
            heappush(self.minheap,num)
        
        if len(self.maxheap)>len(self.minheap)+1:
            heappush(self.minheap,-heappop(self.maxheap))
        elif len(self.maxheap)<len(self.minheap):
            heappush(self.maxheap,-heappop(self.minheap))
    
    def findMedian(self):
        if len(self.maxheap)==len(self.minheap):
            return -self.maxheap[0]/2 +self.minheap[0]/2
        return -self.maxheap[0]

def main():
    FindTheMedian=FindTheMedians()
    FindTheMedian.insertNum(3)
    FindTheMedian.insertNum(1)
    print(FindTheMedian.findMedian())
    print(FindTheMedian.maxheap)
    FindTheMedian.insertNum(5)
    print(FindTheMedian.findMedian())
    print(FindTheMedian.maxheap)
    FindTheMedian.insertNum(3)
    print(FindTheMedian.findMedian())
    print(FindTheMedian.maxheap)
    FindTheMedian.insertNum(7)
    print(FindTheMedian.findMedian())
    print(FindTheMedian.maxheap)
    FindTheMedian.insertNum(4)
    print(FindTheMedian.findMedian())
    print(FindTheMedian.maxheap)
    FindTheMedian.insertNum(2)
    print(FindTheMedian.findMedian())
    print(FindTheMedian.maxheap)
    #This method can not handle the situation when there are duplicated numbers well.

main()