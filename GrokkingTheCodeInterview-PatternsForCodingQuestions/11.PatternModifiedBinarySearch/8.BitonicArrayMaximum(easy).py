#Find the maximum value in a given Bitonic array. 
#An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
#Monotonically increasing or decreasing means that for any index i in the array arr[i]!=arr[i+1].
def Bitonic(array):
    start=0
    end=len(array)-1
    while start<end:
        mid=start+(end-start)//2
        if array[mid]>array[mid+1]:
            end=mid
        elif array[mid]<array[mid+1]:
            start=mid+1
    return array[start]

def main():
    print(Bitonic([1,3,5,6,7,9,6,4,2]))
    print(Bitonic([2,4,6,8,7]))
    print(Bitonic([2,4,6,9]))
    print(Bitonic([7,4,3,2]))

main()