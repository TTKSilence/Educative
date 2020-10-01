#Given an unsorted array containing numbers taken from the range 1 to 'n'.
#The array can have duplicates, which means some numbers will be missing. Find all missing numbers. 

def Findall(array):
    '''Solution1 --For the situation that no duplicates.
    ans=[]
    i=0
    while i<len(array):
        while array[i]!=i+1 and array[i]!=-1:
            while array[i]>len(array):
                array.append(-1)
            swap(i,array[i]-1,array)
        i+=1
    for i in range(len(array)):
        if array[i]==-1:
            ans.append(i+1)
    return ans

    '''
    #Solution2-Educative
    i=0
    while i<len(array):
        if array[i]!=array[array[i]-1]:
            swap(i,array[i]-1,array)
        else:
            i+=1
    ans=[]
    for i in range(len(array)):
        if array[i]!=i+1:
            ans.append(i+1)
    return ans
    
def swap(i,j,array):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp

def main():
    print(Findall([2,2,4,4,6,1])) #3,5
    print(Findall([1,1,4,4])) 
    print(Findall([5,5,5,5,5]))

main()

