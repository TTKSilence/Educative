#Given an array of numbers sorted in ascending order,
#find the element in the array that has the minimum difference with the given 'key'.
#Solution1-Adapted from 'NumberRange'
def MinDiffEle(array,key):
    result=[-1,-1]
    result[0]=Search(array,key,False)
    result[1]=Search(array,key,True)
    return array[result[0]] if abs(array[result[0]]-key)<=abs(array[result[1]]-key) else array[result[1]]

def Search(array,key,MaxIndex):
    Index=-1
    start=0
    end=len(array)-1
    while start<=end:
        mid=start+(end-start)//2
        Index=mid
        if array[mid]<key:
            start=mid+1
        elif array[mid]>key:
            end=mid-1
        else:
            if MaxIndex: #Search forwards to find the last index
                start=mid+1
            else:  #Search backwards to find the first index
                end=mid-1
    return Index
'''
#Solution2-Educative-Adapted from '
def MinDiffEle(array,key):
    if key<=array[0]:
        return array[0]
    if key>=array[-1]:
        return array[-1]
    start=0
    end=len(array)-1
    while start<=end:
        mid=start+(end-start)//2
        if array[mid]<key:
            start=mid+1
        elif array[mid]>key:
            end=mid-1
        else:
            return array[mid]
    return array[start] if abs(array[start]-key)<abs(key-array[end]) else array[end]
'''   

def main():
    print(MinDiffEle([4,6,9,10,12,14],7))
    print(MinDiffEle([4,6,9,10,12,14],4))
    print(MinDiffEle([4,6,9,10,12,14],2))
    print(MinDiffEle([4,6,9,10,12,14],14))
    print(MinDiffEle([4,6,9,10,12,14],17))

main()