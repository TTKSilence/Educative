#Given a set of distinct numbers, find all of its permutations.
#Permutation is defined as the re-arranging of the elements of the set.
from collections import deque
def Permutation(array):
    '''Solution1
    length=len(array)
    perm=[[]]
    for i in range(length):
        count=len(perm)
        for _ in range(count):
            current=perm.pop(0)
            for j in range(i+1):
                temp=list(current)
                temp.insert(j,array[i])
                perm.append(temp)
    return perm
    '''
    #Solution2-Educative
    #length=len(array)
    #result=[]
    permutations=deque()
    permutations.append([])
    for current in array:
        n=len(permutations)
        for _ in range(n):
            oldperm=permutations.popleft()
            for j in range(len(oldperm)+1):
                newperm=list(oldperm)
                newperm.insert(j,current)
                '''
                if len(newperm)==length:
                    result.append(newperm)
                else:
                '''
                permutations.append(newperm)
    #return result
    return list(permutations)



def main():
    print(Permutation([1,3,5]))


main()