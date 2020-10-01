#Given an array of lowcase letters sorted in ascending order,
#find the smallest letter in the given array greater than a given 'key'.
#Assume the given array is a circular list,
#which means that the last letter is assumed to be connected with the first letter.
#This also means that the smallest letter in the given array is greater than the last letter of the array,
#and is also the first letter of the array.
def NextLetter(array,key):
    if array[-1]<=key or array[0]>key:
        return array[0]
    start=0
    end=len(array)-1
    while start<=end:
        mid=start+(end-start)//2
    #Solution1
        if array[mid]<=key:
            if array[mid]==key and array[mid+1]>key:
                return array[mid+1]
            start=mid+1
        elif array[mid]>key:  
            end=mid-1
    return array[start]
    '''
    #Solution2-Educative
        if array[mid]<=key:
            start=mid+1
        else:
            end=mid-1
    return array[start%len(array)]
    '''

def main():
    print(NextLetter(['b','c','e','e','p','t'],'a'))
    print(NextLetter(['b','c','e','e','p','t'],'d'))
    print(NextLetter(['b','c','e','e','p','t'],'e'))
    print(NextLetter(['b','c','e','e','p','t'],'m'))
    print(NextLetter(['b','c','e','e','p','t'],'r'))
    print(NextLetter(['b','c','e','e','p','t'],'t'))
    print(NextLetter(['b','c','e','e','p','t'],'x'))
main()

    