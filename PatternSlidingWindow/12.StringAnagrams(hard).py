import collections
def solution(string,pattern):
    left=0
    count=0
    ans=[]
    pattern_dic=collections.Counter(pattern)
    for i,x in enumerate(string):
        if x in pattern_dic:
            pattern_dic[x]-=1
            if pattern_dic[x]==0:
                count+=1
        
        if count==len(pattern_dic):
            ans.append(left)
        
        if i>=len(pattern)-1:
            if string[left] in pattern_dic:
                if pattern_dic[string[left]]==0:
                    count-=1
                pattern_dic[string[left]]+=1
            left+=1

    return ans

def main():
    print(solution("ppqp","pq"))
    print(solution("abbcabc","abc"))
    print(solution("abdbcbda","abc"))

main()
