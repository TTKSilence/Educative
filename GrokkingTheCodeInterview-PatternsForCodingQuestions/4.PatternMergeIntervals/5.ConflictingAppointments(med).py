#Given an array of intervals representing 'N' appointments, 
#find out if a person can attend all the appointments.

def solution(array):
    array.sort(key=lambda x:x[0])
    for i in range(1,len(array)):
        if array[i-1][1]>array[i][0]:
            return False
    return True

def main():
    print(solution([[1,4],[2,5],[7,9]]))
    print(solution([[6,8],[2,6],[8,12]]))
    print(solution([[4,5],[2,3],[3,6]]))

main()


