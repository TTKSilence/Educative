import collections
def solution(string,pattern):
    #'''My Solution
    pattern_dic=collections.Counter(pattern)
    dic={}
    left=0
    count=0
    for i,x in enumerate(string):
        if x not in pattern_dic:
            left=i+1
            dic.clear()
            count=0
        else:
            if x not in dic:
                dic[x]=0
            dic[x]+=1
            if dic[x]==pattern_dic[x]:
                count+=1
            while dic[x]>pattern_dic[x]:
                if dic[string[left]]==pattern_dic[string[left]]:
                    count-=1
                dic[string[left]]-=1
                left+=1
            if count==len(pattern_dic):
                return True
    return False
    '''
    #Educative's solution
    left=0
    matched=0
    charFrequencyMap=collections.Counter(pattern)
    for i,x in enumerate(string):
        if x in charFrequencyMap:
            charFrequencyMap[x]-=1
            if charFrequencyMap[x]==0:
                matched+=1

        if matched==len(charFrequencyMap):
            return True
        
        if i>=len(pattern)-1:
            if string[left] in charFrequencyMap:
                if charFrequencyMap[string[left]]==0:
                    matched-=1
                charFrequencyMap[string[left]]+=1
            left+=1
    return False
    '''
def main():
    print(solution("oidbcaf","abc"))
    print(solution("odicf","dc"))
    print(solution("bcdxabcdy","bcdyabcdx"))
    print(solution("aaacb","abc"))

main()
