def solution(array,k):
    maxone=0
    left=0
    maxlength=0
    for i,x in enumerate(array):
        if x==1:
            maxone+=1
        if i-left+1-maxone>k:
            if array[left]==1:
                maxone-=1
            left+=1
        maxlength=max(maxlength,i-left+1)
    return maxlength

def main():
    print(solution([0,1,1,0,0,0,1,1,0,1,1],2))
    print(solution([0,1,0,0,1,1,0,1,1,0,0,1,1],3))

main()