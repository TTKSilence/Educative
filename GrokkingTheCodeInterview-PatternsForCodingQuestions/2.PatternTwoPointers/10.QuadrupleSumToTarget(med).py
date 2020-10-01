#Given an array of unsorted numbers and a target number, 
#find all unique quadruples in it, whose sum is equal to the target number.
def quadruples(array,target):
    ans=[]
    array.sort()
    for first in range(len(array)-3):
        if first>0 and array[first]==array[first-1]:
            continue
        tri_sum=target-array[first]
        searchTriples(array,first,tri_sum,ans)
    return ans

def searchTriples(array,first,target,ans):
    for second in range(first+1,len(array)-2):
        if second>0 and array[second]==array[second-1]:
            continue
        pai_sum=target-array[second]
        searchPairs(array,first,second,pai_sum,ans)

def searchPairs(array,first,second,target,ans):
    third=second+1
    fourth=len(array)-1
    while third<fourth:
        temp=array[third]+array[fourth]
        if temp==target:
            ans.append([array[first],array[second],array[third],array[fourth]])
            third+=1
            while array[third]==array[third-1] and third<fourth:
                third+=1
        elif temp<target:
            third+=1
        else:
            fourth-=1

def main():
    print(quadruples([4,1,2,-1,-3,1,-3],1))
    print(quadruples([2,0,-1,-2,1,-2,2],2))

main()

    

    
