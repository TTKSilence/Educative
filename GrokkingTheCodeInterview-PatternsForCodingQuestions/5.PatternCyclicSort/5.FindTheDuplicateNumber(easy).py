#Given an unsorted array containing 'n+1' numbers taken from the range 1 to 'n'.
#The array has only one duplicate but it can be repeated multiple times.
#Find that duplicate number without using any extra space.

def Findduplicate(array):
    for i in range(len(array)):
        while array[i]!=i+1:
            if array[i]==array[array[i]-1]:
                return array[i]
            swap(i,array[i]-1,array)
    return -1

def swap(i,j,array):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp

def main():
    print(Findduplicate([1,4,4,3,2]))
    print(Findduplicate([1,3,4,4,4]))
    print(Findduplicate([4,4,4,4,4]))

main()