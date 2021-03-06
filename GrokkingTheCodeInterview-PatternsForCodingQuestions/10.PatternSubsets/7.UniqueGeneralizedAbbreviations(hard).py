#Given a word, write a function to generate all of its unique generalized abbreviations.
#Generalized abbreviation of a word can be generated by replacing each substring of the word by
#the count of characters in the substring.
#Solution1 - BFS
from collections import deque
class Abbreviation:
    def __init__(self,str,start,count):
        self.str=str
        self.start=start #the index of the next char in the str 'word'
        self.count=count #the number of the replaced char after the last preserved char
    
def generate(word):
    wordlen=len(word)
    result=[]
    queue=deque()
    queue.append(Abbreviation(list(),0,0))
    while queue:
        abword=queue.popleft()
        if abword.start==wordlen:
            if abword.count!=0:
                abword.str.append(str(abword.count))
            result.append(''.join(abword.str))
        else:
            #add 'count' instead of changing the current str
            queue.append(Abbreviation(list(abword.str),abword.start+1,abword.count+1)) 
            #add the new char in the current str instead of increasing the 'count'
            if abword.count!=0: #turn the 'count' into the digit char if there exists
                abword.str.append(str(abword.count))
            newword=list(abword.str)
            newword.append(word[abword.start])
            queue.append(Abbreviation(newword,abword.start+1,0))
    return result
'''

#Solution2 - Recursion

def generate(word):
    result=[]
    abbreviation(word,list(),0,0,result)
    return result

def abbreviation(word,abword,start,count,result):
    if start==len(word):
        if count!=0:
            abword.append(str(count))
        result.append(''.join(abword))
    else:
        abbreviation(word,list(abword),start+1,count+1,result)
        if count!=0:
            abword.append(str(count))
        newword=list(abword)
        newword.append(word[start])
        abbreviation(word,newword,start+1,0,result)
'''
def main():
    print(generate('BAT'))
    print(generate(''))
    print(generate('code'))

main()