#Given a string, sort it based on the decreasing frequency of its characters.
from collections import Counter
from heapq import *
def FrequencySort(str):
    freqdict=Counter(str)
    '''Solution1
    minheap=[]
    for char,freq in freqdict.items():
        heappush(minheap,(freq,char))
    result=''
    while minheap:
        temp=heappop(minheap)
        for _ in range(temp[0]):
            result=temp[1]+result
    return result
    '''
    #Solution2-Educative
    maxheap=[]
    for char,freq in freqdict.items():
        heappush(maxheap,(-freq,char))
    result=[]
    while maxheap:
        freq,char=heappop(maxheap)
        for _ in range(-freq):
            result.append(char)
    return ''.join(result)

def main():
    print(FrequencySort('Programming'))
    print(FrequencySort('abcbcacca'))
    print(FrequencySort('AbcbcaCca'))

main()

