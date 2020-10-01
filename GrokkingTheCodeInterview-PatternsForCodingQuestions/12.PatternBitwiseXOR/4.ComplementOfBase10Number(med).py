#Every non-negative integer N has a binary representation.
#The complement of a binary representation is the number in binary that
#we get when we change every 1 to a 0 and every 0 to a 1.
#For a given positive number N in base-10,
#return the complement of its binary representation as a base-10 integer.

def NumberComplement(num):     
    count=0 if num>0 else 1        #1^0=1; 1^1=0; ——> 1^(0 / 1)=1 / 0 ——> 11...1 ^ num=complement
    n=num                          #11...1 ^ num ^num =11...1 =complement ^ num
    while n>0:
        count+=1
        n=n>>1
    allbitsset=pow(2,count)-1 #allbitsset means that all the bits equal to 1
    return allbitsset^num  # num^complement=allbitsset

def main():
    print(NumberComplement(8))
    print(NumberComplement(0))

main()