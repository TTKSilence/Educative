#Given an array of unsorted numbers and find a triplet in the array whose sum is as close to the target number
#as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the
#sum of the triplet with the triplet with the smallest sum.

def solution(array, target):
    array.sort()
    first=0
    ans=float('inf')
    for first in range(len(array)-2):
        ans=helper(array,first,ans,target)
        if ans==0:
            break
    return ans

def helper(array,first,ans,target):
    second=first+1
    third=len(array)-1
    while second<third:
        temp=array[first]+array[second]+array[third]
        if abs(temp-target)<abs(ans-target) or (abs(temp-target)==abs(ans-target) and temp<ans):
            ans=temp
        if temp>target:
            third-=1
        elif temp<target:
            second+=1
    return ans
    
def main():
    print(solution([-2,0,1,2],2))
    print(solution([-3,-1,1,2],1))
    print(solution([1,0,1,1],100))

main()



