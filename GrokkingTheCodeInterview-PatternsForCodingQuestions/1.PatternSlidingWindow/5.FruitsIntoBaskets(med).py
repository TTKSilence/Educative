def solution(Fruit):
    left=0
    basket={}
    count=0
    maxlength=0
    for i,x in enumerate(Fruit):
        if x in basket:
            basket[x]+=1
        else:
            basket[x]=1
            count+=1
        while count>2:
            basket[Fruit[left]]-=1
            if basket[Fruit[left]]==0:
                del basket[Fruit[left]]
                count-=1
            left+=1
        maxlength=max(maxlength,i-left+1)
    return maxlength

def main():
    print(solution(['A','B','C','A','C']))
    print(solution(['A','B','C','B','B','C']))

main()