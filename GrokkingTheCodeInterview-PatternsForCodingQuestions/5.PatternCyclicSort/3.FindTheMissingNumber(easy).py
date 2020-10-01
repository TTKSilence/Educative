#Given an array containing 'n' distinct numbers taken from the range 0 to 'n'.
#Since the array has only 'n' numbers out of the total 'n+1' numbers, find the missing number.

def Find(array):
    '''Solution1
    array.append(-1)
    for i in range(len(array)):
        while array[i]!=i and array[i]!=-1:
            swap(i,array[i],array)
    return array.index(-1)
    '''
    #Solution2-Educative
    i=0
    while i<len(array):
        if array[i]<len(array) and array[i]!=i:
            swap(i,array[i],array)
        else:
            i+=1
    for i in range(len(array)):
        if array[i]!=i:
            return i
    return len(array)

def swap(i,j,array):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp

def main():
    print(Find([2,4,6,0,3,1]))
    print(Find([1,4,2,5,3,6]))
    print(Find([1,2,3,4,5,0]))

main()

