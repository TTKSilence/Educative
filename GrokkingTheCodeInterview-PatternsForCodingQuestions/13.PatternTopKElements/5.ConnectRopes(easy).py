#Given 'N' ropes with different lengths,
#we need to connect these ropes into one big rope with minimum cost.
#The cost of connecting two ropes is equal to the sum of their lengths.
from heapq import *
def ConnectRopes(array):
    minheap=[]
    for i in range(len(array)):
        heappush(minheap,array[i])
    
    result=0
    temp=0
    while len(minheap)>1:
        temp=heappop(minheap)+heappop(minheap)
        result+=temp
        heappush(minheap,temp)
    
    return result

def main():
    print(ConnectRopes([2,5,3,6,46,23,75]))
    print(ConnectRopes([23,4,62,32]))
    print(ConnectRopes([1,3,11,5,2]))

main()


