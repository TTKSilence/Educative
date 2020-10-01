#Given a sorted number array and two integers 'K' and 'X',
#find 'K' closest numbers to 'X' in the array.
#Return the numbers in the sorted order. 'X' is not necessarily present in the array.
from heapq import *
def KClosestNumbers(array,K,X):
    '''Solution1
    numdis={}
    count={}
    for i in array:
        numdis[i]=-abs(X-i)
        if i not in count:
            count[i]=1
        else:
            count[i]+=1
    maxheap=[]
    for num,dis in numdis.items():
        for _ in range(count[num]):
            heappush(maxheap,(dis,num))
        while len(maxheap)>K:
            heappop(maxheap)
    result=[]
    for temp in maxheap:
        result.append(temp[1])
    return result
    '''
    #Solution2-Educative
    left=0
    right=len(array)
    while left<=right:
        mid=left+(right-left)//2
        if array[mid]>X:
            right=mid-1
        elif array[mid]<X:
            left=mid+1
        else:
            break
    left=max(0,mid-K)
    right=min(len(array),mid+K)
    minheap=[]
    for i in range(left,right+1):
        heappush(minheap,(abs(array[i]-X),array[i]))
    result=[]
    for _ in range(K):
        result.append(heappop(minheap)[1])
    return result

def main():
    print(KClosestNumbers([2,5,3,7,8,9,4],3,6))
    print(KClosestNumbers([2,5,3,7,7,8,9,4],2,6))
    print(KClosestNumbers([2,5,3,6,7,8,9,4],4,6))

main()

