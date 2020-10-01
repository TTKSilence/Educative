#Given two lists of intervals, find the intersection of two lists. 
#Each list consists of disjoint intervals sorted on their start time.

def solution(array1,array2):
    array1.sort(key=lambda x: x[0])
    array2.sort(key=lambda x: x[0])
    ind1,ind2=0,0
    start,end=0,0
    result=[]
    while ind1<len(array1) and ind2<len(array2):
        if array1[ind1][1]<array2[ind2][0]:
            ind1+=1
        elif array1[ind1][0]>array2[ind2][1]:
            ind2+=1
        else:
            start=max(array1[ind1][0],array2[ind2][0])
            end=min(array1[ind1][1],array2[ind2][1])
            result.append([start,end])
            if array1[ind1][1]<array2[ind2][1]:
                ind1+=1
            else:
                ind2+=1

    return result
def main():
    print(solution([[5,6],[1,3],[7,9]],[[2,3],[5,7]]))
    print(solution([[9,12],[1,3],[5,7]],[[5,10]]))

main()
    