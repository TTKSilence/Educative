#Given an array containing 'n' objects, 
#Each object, when created, was assigned a unique number from 1 to 'n' based on their creation sequence.
#Write a function to sort the objects in-place on their creation sequence number in O(n)
#and without any extra space. 
#Assume passed an integer array containing only the sequence number.

def CyclicSort(array):
    for i in range(len(array)):
        while array[i]!=i+1:
            swap(i,array[i]-1,array)
    return array

def swap(i,j,array):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp

def main():
    print(CyclicSort([2,4,6,5,3,1]))
    print(CyclicSort([1,4,2,5,3,6]))
    print(CyclicSort([1,2,3,4,5,6]))

main()
