#Given an array of unsorted numbers and a target sum, 
#count all triplets in it such that the sum of the triplet is less than the given target
def solution(array,target):
    '''Solution1
    array.sort()
    num=0
    for first in range(len(array)):
        second=first+1
        third=len(array)-1
        temp=target-array[first]
        while second<third:
            if array[second]+array[third]<temp:
                num+=third-second
                second+=1
            else:
                third-=1
    return num
    ''' 
    
    #Solution2
    array.sort()
    num=0
    for first in range(len(array)):
        temp=target-array[first]
        num+=searchPair(array,first,temp)
    return num
def searchPair(array,first,temp):
    second=first+1
    third=len(array)-1
    num=0
    while second<third:
        if array[second]+array[third]<temp:
            num+=third-second
            second+=1
        else:
            third-=1
    return num

def main():
    print(solution([-1,0,2,3],3))
    print(solution([-1,4,2,1,3],5))

main()