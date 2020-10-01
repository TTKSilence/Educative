#Given a sorted array, 
#create a new array containing squares of all the number of the input array in the sorted order.

def solution(array):
    left=0
    right=len(array)-1
    ans=[]
    while left<=right:
        left2=array[left]*array[left]
        right2=array[right]*array[right]
        if left2<=right2:
            ans.insert(0,right2)    #ans.append(right2)
            right-=1
        else:
            ans.insert(0,left2)    #ans.append(left2)
            left+=1
    return ans    #ans[::-1]

def main():
    print(solution([-2,-1,0,2,3]))
    print(solution([-5,-3,-1,2,4]))

main()

            


