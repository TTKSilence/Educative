def Function(s,array):
    sum=0
    ans=len(array)+1
    j=0
    for i in range(len(array)):
        sum+=array[i]
        while sum>=s:
            ans=min(ans,i-j+1)
            sum-=array[j]
            j+=1
    return ans if ans!=len(array)+1 else 0

def main():
    print(Function(7,[2,1,5,2,3,2]))
    print(Function(7,[2,1,5,2,8]))
    print(Function(8,[3,4,1,1,6]))

main()
        

