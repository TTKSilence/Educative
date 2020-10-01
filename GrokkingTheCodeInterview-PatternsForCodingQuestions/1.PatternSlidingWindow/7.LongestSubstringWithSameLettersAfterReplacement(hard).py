def solution(string,k):
    '''Solution1
    count=0
    maxlength=0
    left=0
    cur=0
    while left<len(string):
        while count<=k and left+cur<len(string):
            if string[cur+left]!=string[left]:
                count+=1
            cur+=1
        if count>k:
            cur-=1
        maxlength=max(maxlength,cur)
        left+=1
        count=0
        cur=0
    return maxlength
    '''
    #Solution2
    left=0
    maxrepeat=0
    maxlength=0
    dic={}
    for i,x in enumerate(string):
        if x not in dic:
            dic[x]=0
        dic[x]+=1
        maxrepeat=max(maxrepeat,dic[x])
        if i-left+1-maxrepeat>k:
            dic[string[left]]-=1
            left+=1
        maxlength=max(maxlength,i-left+1)
    return maxlength

def main():
    print(solution("aabccbb",2))
    print(solution("abbcb",1))
    print(solution("aaccde",1))

main()
