#Given an unsorted array containing 'n' numbers taken from the range 1 to 'n'.
#The array originally contained all the numbers from 1 to 'n', but due to a data error,
#one of the numbers got duplicated which also resulted in one number going missing.
#Find both these numbers.

def CorruptPair(array):
    num=0
    for i in range(len(array)):
        while array[i]!=i+1:
            if array[i]==array[array[i]-1]:
                num=i
                break
            swap(i,array[i]-1,array)
    return [array[num],num+1]
    
def swap(i,j,array):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp

def main():
    print(CorruptPair([3,1,2,5,2]))
    print(CorruptPair([3,1,2,3,6,4]))

main()