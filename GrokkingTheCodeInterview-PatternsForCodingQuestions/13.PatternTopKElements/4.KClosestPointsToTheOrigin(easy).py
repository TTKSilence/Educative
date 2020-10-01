#Given an array of points in the a 2D plane, find 'k' closest points to the origin.
from heapq import *
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #the key part to achieve the maxheap 
    def __lt__(self,other):
        return self.dis() > other.dis()
    
    def dis(self):
        return(self.x*self.x+self.y*self.y)
    
    def print_point(self):
        print('['+str(self.x)+','+str(self.y)+']',end='')


def KClosestPoints(points,k):
    maxheap=[]
    for i in range(k):
        heappush(maxheap,points[i])
    
    for i in range(k,len(points)):
        if points[i].dis()<maxheap[0].dis():
            heappop(maxheap)
            heappush(maxheap,points[i])
    
    return list(maxheap)

def main():
    res=KClosestPoints([Point(2,3),Point(5,8),Point(8,9),Point(5,8),Point(7,8),Point(4,5)],5)
    for point in res:
        point.print_point()

main()
    