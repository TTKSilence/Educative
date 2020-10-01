#In a non-empty array of numbers,
#every number appears exactly twice except two numbers that appear only once.
#Find the two numbers that appear only once.
def TwoSingleNumbers(array):
    x=array[0]
    for i in array[1:]:
        x^=i
    #print(bin(x))

    #Find out the different bit from right to left between these two nums which is in binary.
    rightmostbit=1
    while (rightmostbit & x)==0:
        rightmostbit=rightmostbit<<1
    #print(bin(rightmostbit))
    
    #Other nums except n1 and n2 can be eliminated because they appear twice.
    n1,n2=0,0
    for n in array:
        if (n & rightmostbit)!=0:
            n1^=n
        else:
            n2^=n
    return [n1,n2]
    #return [bin(n1),bin(n2)]

def main():
    print(TwoSingleNumbers([2,5,3,7,8,9,13,16,9,13,3,5,8,7]))
    print(TwoSingleNumbers([3,5,9,1,9,5,1,6]))
    print(TwoSingleNumbers([4,7]))

main()