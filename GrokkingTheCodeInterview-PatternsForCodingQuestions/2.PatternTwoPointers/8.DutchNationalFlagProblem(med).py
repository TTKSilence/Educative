#Given an array containing 0s, 1s and 2s, sort the array in-place.
#Since the numbers of the array should be treated as objects, 
#hence, we can't count 0s, 1s and 2s to recreat the array.

def solution(array):
    left=0
    right=len(array)-1
    i=0
    while i<=right:
        if array[i]==0:
            swap(array,i,left)
            left+=1
            i+=1
        elif array[i]==1:
            i+=1
        else:
            swap(array,i,right)
            right-=1
    return array
def swap(array,m,n):
    temp=array[m]
    array[m]=array[n]
    array[n]=temp

def main():
    print(solution([1,0,2,1,0]))
    print(solution([2,2,0,1,2,0]))
    print(solution([1,1,1,1]))

main()
        