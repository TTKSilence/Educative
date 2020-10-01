#Given an array of numbers sorted in an ascending order, find the ceiling of a given number 'key'.
#The ceiling of the 'key' will be the smallest element in the given array greater than or equal to 'key'.
#Write a function to return the index of the ceiling of the 'key'. If there isn't any ceiling return -1.
def Search(array,key):
    '''Solution1
    left=0
    right=len(array)-1
    while left<=right:
        middle=left+(right-left)//2
        if array[middle]>=key:
            if middle==0 or array[middle-1]<key:
                return middle
            else:
                right=middle-1
        else:
            left=middle+1
    return -1
    '''
    #Solution2-Educative
    if key>array[-1]:
        return -1
    left=0
    right=len(array)-1
    while left<=right:
        middle=left+(right-left)//2
        if array[middle]>key:
            right=middle-1
        elif array[middle]<key:
            left=middle+1
        else:
            return middle #there exists a bug when the array contains duplicate keys.
    return left
    

def main():
    print(Search([4,7,8,10],9))
    print(Search([4,5,5,7,8,10],5))
    print(Search([4,7,8,10],1))
    print(Search([4,7,8,10],12))

main()