#Given a string,
#find if its letters can be rearranged in such a way that no two same characters come next to each other.
from collections import Counter
from heapq import *
def RearrangedString(str):
    maxheap=[]
    charfreq=Counter(str)
    for char, freq in charfreq.items():
        heappush(maxheap,(-freq,char))
    result=''
    prevfreq,prevchar=0,None
    while maxheap:
        curfreq,curchar=heappop(maxheap)
        if prevfreq<0:
            heappush(maxheap,(prevfreq,prevchar))
        result+=curchar
        prevfreq,prevchar=curfreq+1,curchar
    return result if  len(result)==len(str) else ''

def main():
    print(RearrangedString('programming'))
    print(RearrangedString('aaapkpaa'))

main()

        


    
