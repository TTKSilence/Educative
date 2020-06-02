def solution(string,k):
    j=0
    dic={}
    num=0
    ans=0
    for i,x in enumerate(string):
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1
            num+=1
        while num>k:
            dic[string[j]]-=1
            if dic[string[j]]==0:
                del dic[string[j]]
                num-=1
            j+=1
        ans=max(ans,i-j+1)
    return ans

def main():
    print(solution("araaci",2))
    print(solution("araaci",1))
    print(solution("cbbebi",3))

main()
                
                
