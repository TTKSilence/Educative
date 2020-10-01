#Given an unsorted array containing 'n' numbers taken from 1 to 'n'. 
#The array has some duplicates, find all the duplicate numbers without using any extra space.

def FindAllDuplicates(array):
    ans=[]
    '''Solution1
    for i in range(len(array)):
        if array[i] not in ans:
            while array[i]!=i+1:
                if array[i]!=array[array[i]-1]:
                    swap(i,array[i]-1,array)
                else:
                    ans.append(array[i])
                    break
    '''
    #Solution2_Educative:
    i=0
    while i<len(array):
        if array[i]!=array[array[i]-1]:
            swap(i,array[i]-1,array)
        else:
            i+=1
    
    for i in range(len(array)):
        if array[i]!=i+1:
            ans.append(array[i])
            
    return ans

def swap(i,j,array):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp

def main():
    print(FindAllDuplicates([2,2,4,4,5,5]))
    print(FindAllDuplicates([5,5,4,4,3,6,6]))

main()
            