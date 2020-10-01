#Given an N*N matrix where each row and column is sorted in ascending order, 
#find the Kth smallest element in the matrix.
from heapq import *
def KthSmallestNumInMatrix(matrix,k):
    minheap=[]
    for i in range(min(k,len(matrix))):
        heappush(minheap,(matrix[i][0],0,i))   
    count=0
    length=len(matrix[0])
    while minheap:
        num,column,row=heappop(minheap)
        count+=1
        if count==k:
            break
        if column<length-1:
            heappush(minheap,(matrix[row][column+1],column+1,row))
    return num

def main():
    print(KthSmallestNumInMatrix([[0,3,6,9],[1,4,7,10],[2,5,8,11]],9))

main()
