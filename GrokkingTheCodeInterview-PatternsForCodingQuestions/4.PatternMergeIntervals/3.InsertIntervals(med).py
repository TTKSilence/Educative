#Given a list of non-overlapping intervals sorted by their start time, 
#insert a given interval at the correct position 
#and merge all necessary intervals to produce a list that has only mutually exclusive intervals.
class Interval:
    def __init__(self, start, end):
        self.start=start
        self.end=end

    def print_interval(self):
        print("["+ str(self.start)+","+str(self.end)+"]",end='')

def solution(Intervals, NewInterval):
    '''Solution1
    i=0
    while i<len(Intervals):
        if Intervals[i].start>=NewInterval.start:
            Intervals.insert(i,NewInterval)
            break
        i+=1
    if i==len(Intervals):
        Intervals.append(NewInterval)
    Result=[] #the results returned
    start=Intervals[0].start
    end=Intervals[0].end
    for i in range(1,len(Intervals)):
        inter=Intervals[i]
        if inter.start<end: #overlapping
            end=max(inter.end,end)
        else: #no-overlapping
            Result.append(Interval(start,end))
            start=inter.start
            end=inter.end
    Result.append(Interval(start,end)) #the last one
    return Result
    '''
    #Solution2
    merged=[]
    i=0
    while i<len(Intervals) and Intervals[i].end<NewInterval.start:
        merged.append(Intervals[i])
        i+=1
    
    while i<len(Intervals) and Intervals[i].start<=NewInterval.end:
        NewInterval.start=min(Intervals[i].start, NewInterval.start)
        NewInterval.end=max(Intervals[i].end,NewInterval.end)
        i+=1
    merged.append(NewInterval)

    while i<len(Intervals):
        merged.append(Intervals[i])
        i+=1
    return merged
    


def main():
    for i in solution([Interval(1,3),Interval(4,5),Interval(7,9)], Interval(4,6)):
        i.print_interval()
    print()
    
    for i in solution([Interval(2,4),Interval(7,9),Interval(11,13)], Interval(2,11)):
        i.print_interval()
    print()

    for i in solution([Interval(2,4),Interval(6,9),Interval(11,12)], Interval(1,13)):
        i.print_interval()
    print()
    
main()