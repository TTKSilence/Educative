#Given an infinite sorted array (or an array with unknow size),
#find if a given number 'key' is present in the array.
#Write a function to return the index of the 'key' if it is present in the array, otherwise return -1.
def Search(array,key):
    if array[0]>key:
        return -1
    start,end=0,1
    size=2
    while array[end]<key:
        size=2*size
        start=end+1
        end=start+size

    while start<=end:
        mid=start+(end-start)//2
        if array[mid]<key:
            start=mid+1
        else:
            index=mid
            end=mid-1
    return index if array[index]==key else -1

def main():
    print(Search([4,6,8,9,9,10,13,15,17,18,23,27,29,34,38,46,57],9))
    print(Search([4,6,8,9,9,10,13,15,17,18,23,27,29,34,47,57,86],18))
    print(Search([4,6,8,9,10,13,15,18,23,23,23,27,29,34,46,57,57,67],23))
    print(Search([4,4,6,8,9,9,10,13,15,17,23,29,34,37,56,57,58,68,69],4))
    print(Search([4,6,8,9,9,10,13,15,17,18,23,27,34,37,45,47,48,58,68],16))

main()