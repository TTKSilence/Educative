#Given an array of numbers sorted in ascending order, find the range of a given number 'key'.
#The range of the 'key' will be the first and last position of the 'key' in the array.
#Write a function to return the range of the 'key'. If the 'key' is not present return [-1,-1].
'''Solution1
def NumberRange(array,key):
    if not array or key<array[0] or key>array[-1]:
        return [-1,-1]
    start=0
    end=len(array)-1
    while start<=end:
        mid=start+(end-start)//2
        if array[mid]<=key:
            start=mid+1
        else:
            end=mid-1
    if array[end]<key:
        return [-1,-1]
    i=end
    while i>=0 and array[i]>=key:
        i-=1
    return [i+1,end]
'''
#Solution2-Educative
def NumberRange(array,key):
    result=[-1,-1]
    result[0]=Search(array,key,False)
    if result[0]!=-1:
        result[1]=Search(array,key,True)
    return result

def Search(array,key,MaxIndex):
    KeyIndex=-1
    start=0
    end=len(array)-1
    while start<=end:
        mid=start+(end-start)//2
        if array[mid]<key:
            start=mid+1
        elif array[mid]>key:
            end=mid-1
        else:
            KeyIndex=mid
            if MaxIndex: #Search forwards to find the last index
                start=mid+1
            else:  #Search backwards to find the first index
                end=mid-1
    return KeyIndex

def main():
    print(NumberRange([4,6,6,6,9],6))
    print(NumberRange([4,4,6,6,9],4))
    print(NumberRange([4,6,9,9,9],9))
    print(NumberRange([6,6,6,6,6],6))
    print(NumberRange([4,6,6,6,9],5))
    print(NumberRange([],6))

main()
    