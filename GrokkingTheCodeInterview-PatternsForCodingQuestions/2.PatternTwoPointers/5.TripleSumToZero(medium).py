#Given an array of unsorted numbers,
#find all unique triples in it that add up to zero.

def solution(array):
    '''Soluton1--Silly one
    array.sort()
    first=0
    ans=[]
    while first<len(array)-2 and array[first]<=0:
        second=first+1
        while second<len(array)-1 and array[first]+array[second]<=0:
            if -(array[first]+array[second]) in array[second+1:]:
                ans.append([array[first],array[second],-(array[first]+array[second])])
            while array[second+1]==array[second]:
                second+=1
            second+=1
        first+=1
    return ans
    '''

    #Solution2
    array.sort()
    ans=[]
    for first in range(len(array)-2):
        if array[first]>0:
            break
        if first>0 and array[first]==array[first-1]:
            continue
        PairWithTargetSum(array,first,-array[first],ans)
    return ans
    
def PairWithTargetSum(array,first,target,ans):
    second=first+1
    third=len(array)-1
    while second<third:
        temp=array[second]+array[third]
        if temp==target:
            ans.append([array[first],array[second],array[third]])
            second+=1
            third-=1
            while temp<target and array[second]==array[second-1]:
                second+=1
            while temp>target and array[third]==array[third+1]:
                third-=1
        elif temp<target:
            second+=1
        else:
            third-=1
            
def main():
    print(solution([-3,0,1,2,-1,1,-2]))
    print(solution([-5,2,-1,-2,3]))

main()
