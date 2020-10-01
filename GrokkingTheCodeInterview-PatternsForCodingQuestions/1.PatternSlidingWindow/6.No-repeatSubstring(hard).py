def solution(string):
    '''Solution1:
    dic={}
    left=0
    maxlength=0
    for i,x in enumerate(string):
        if x not in dic:
            dic[x]=0
        dic[x]+=1
        while dic[x]>1:
            dic[string[left]]-=1
            left+=1
        maxlength=max(maxlength,i-left+1)
    return maxlength
    '''
    #Solution2
    dic={}
    left=0
    maxlength=0
    for i,x in enumerate(string):
        if x in dic:
            left=max(left,dic[x]+1)
        dic[x]=i
        maxlength=max(maxlength,i-left+1)
    return maxlength

def main():
    print(solution("aabccbb"))
    print(solution("abbbb"))
    print(solution("abccde"))

main()
