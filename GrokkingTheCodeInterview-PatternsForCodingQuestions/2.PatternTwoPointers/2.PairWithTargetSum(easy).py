# Given an array of sorted numbers and a target sum, 
# find a pair in the array whose sum is equal to the given target.
def solution(array, target):
    left=0
    right=len(array)-1
    ans=[]
    while left<right and left>=0 and right<len(array):
        if array[left]+array[right]==target:
            ans.append([left,right])
        if array[left]+array[right]<target:
            left+=1
        else:
            right-=1
    return ans

def main():
    print(solution([1,2,3,4,6],6))
    print(solution([2,5,9,11],11))
    print(solution([1,3,4,6],11))

main()