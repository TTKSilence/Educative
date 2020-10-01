#Given a list of intervals representing the start and end time of 'N' meetings,
#find the minimum number of rooms required to hold all the meetings.
from heapq import *
def MinRooms(array):
    array.sort(key=lambda x: x[0])
    '''Solution1
    ends=[array[0][1]]
    for i in array[1:]:
        mini=min(ends)
        if i[0]>=mini:
            ends.remove(mini)
        ends.append(i[1])
    return len(ends)
    '''
    #Solution2
    minrooms=0
    minheap=[array[0][1]]
    for i in array[1:]:
        while minheap and i[0]>=minheap[0]:
            heappop(minheap)
        heappush(minheap,i[1])
        minrooms=max(minrooms,len(minheap))
    return minrooms




def main():
    print(MinRooms([[1,4],[1,5],[4,9],[4,5]]))
    print(MinRooms([[6,7],[2,4],[8,12]]))
    print(MinRooms([[1,4],[2,3],[3,6]]))
    print(MinRooms([[4,5],[2,3],[2,4],[3,5]]))

main()