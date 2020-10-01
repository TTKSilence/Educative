#Given an array of sorted numbers, remove all duplicates from it.
#Don't use any extra space. After removing the duplicates in-place return the new length of the array.

def solution(array):
    NoDuplicate=1
    for x in array:
        if array[NoDuplicate-1]!=x:
            array[NoDuplicate]=x
            NoDuplicate+=1
    del array[NoDuplicate:]
    return len(array)

def main():
    print(solution([2,3,3,3,4,6,6,9]))
    print(solution([2,3,3,3,6,6,9]))
    print(solution([2,2,2,9]))
    print(solution([2,3,4,6,9]))

main()
            

        