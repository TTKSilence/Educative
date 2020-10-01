#Given a string and a pattern,
#find the smallest substring in the given string which has all the characters of the given pattern.
from collections import Counter
def SmallestWindow(string,pattern):
    #'''Solution1
    p_dict=Counter(pattern)
    left,right=0,0
    ans=''
    length=len(string)+1
    count=len(p_dict)
    for right in range(len(string)):
        if string[right] in p_dict:
            p_dict[string[right]]-=1
            if p_dict[string[right]]==0:
                count-=1
            while p_dict[string[right]]<0:
                if string[left] in p_dict:
                    p_dict[string[left]]+=1
                    if p_dict[string[left]]==1:
                        count+=1
                left+=1
            if count==0 and length>right-left+1:
                ans=string[left:right+1]
                length=right-left+1
    return ans
    '''
    #Solution2-Educaive
    p_dict=Counter(pattern)
    left,right=0,0
    subleft=0
    length=len(string)+1
    count=len(p_dict)
    for right in range(len(string)):
        if string[right] in p_dict:
            p_dict[string[right]]-=1
            if p_dict[string[right]]==0:
                count-=1
        while count==0:
            if length>right-left+1:
                length=right-left+1
                subleft=left
            leftchar=string[left]
            left+=1
            if leftchar in p_dict:
                if p_dict[leftchar]==0:
                    count+=1
                p_dict[leftchar]+=1
    return string[subleft:subleft+length] if length<=len(string) else ''                   
    '''

def main():
    print(SmallestWindow('aabecadb','abc'))
    print(SmallestWindow('abdabca','abc'))
    print(SmallestWindow('aabdec','abf'))

main()


    
