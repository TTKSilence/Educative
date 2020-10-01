#Given a sorted array of numbers, find if a given number 'key' is present in the array.
#Whether the array is sorted in ascending or descending order is unknown.
#The array can have duplicates.
#Write a function to return the index of the 'key' if it is present in the array, otherwise return -1.
def Search(array,key):
    ascending=True if array[0]<=array[-1] else False
    left=0
    right=len(array)-1
    while left<=right:
        middle=left+(right-left)//2
        if array[middle]==key:
            return middle
        if ascending:
            if array[middle]<key:
                left=middle+1
            else:
                right=middle-1
        else:
            if array[middle]<key:
                right=middle-1
            else:
                left=middle+1
    return -1

def main():
    print(Search([4,7,8,10],7))
    print(Search([6,4,3,2,1],6))
    print(Search([6,4,3,2,1],1))
    print(Search([6,4,3,1,0],2))

main()