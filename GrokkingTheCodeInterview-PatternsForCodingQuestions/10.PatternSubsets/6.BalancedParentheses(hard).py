#For a given number 'N', write a function to generate all combination of 'N' pairs of balanced parentheses.
#Solution1 - BFS
from collections import deque
class parenthese:
    def __init__(self,str,opencount,closecount):
        self.str=str
        self.opencount=opencount
        self.closecount=closecount

def BalancedParenthese(n):
    result=[]
    queue=deque()
    queue.append(parenthese('',0,0))
    while queue:
        current=queue.popleft()
        if current.opencount==current.closecount==n:
            result.append(current.str)
        else:
            if current.opencount<n:
                queue.append(parenthese(current.str+'(',current.opencount+1,current.closecount))
            if current.closecount<current.opencount:
                queue.append(parenthese(current.str+')',current.opencount,current.closecount+1))
    return result

'''#Solution2 - Recursion
def BalancedParenthese(n):
    result=[]
    parenthese=[0]*2*n
    GenerateParenthese(n,0,0,parenthese,0,result)
    return result

def GenerateParenthese(n,opencount,closecount,parenthese,index,result):
    if opencount==closecount==n:
        result.append(''.join(parenthese))
    else:
        if opencount<n:
            parenthese[index]='('
            GenerateParenthese(n,opencount+1,closecount,parenthese,index+1,result)
        if opencount>closecount:
            parenthese[index]=')'
            GenerateParenthese(n,opencount,closecount+1,parenthese,index+1,result)
'''

def main():
    print(BalancedParenthese(2))
    print(BalancedParenthese(3))

main()

''' #bugs in it, may be valuable, or not.
    for i in range(1,n):
        length=len(parenthese)
        for _ in range(length):
            current=res.popleft()
            count=len(current)
            number=i #the remaining number of the left-part parenthese
            j=1
            while j<count and number>0:
                if current[j-1]=='(':
                    number-=1
                temp=list(current)
                temp.insert(j,'()')
                res.append(''.join(temp))
                j+=1
    return res
'''


