#Given a list of intervals, 
#merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

class Interval:
    def __init__(self, start, end):
        self.start=start
        self.end=end

    def print_interval(self):
        print("["+ str(self.start)+","+str(self.end)+"]",end='')
    
def solution(intervals):
    if len(intervals)<2:
        return intervals
    #sort the intervals
    intervals.sort(key=lambda x: x.start)
    mergedIntervals=[] #the results returned
    start=intervals[0].start
    end=intervals[0].end
    for i in range(1,len(intervals)):
        inter=intervals[i]
        if inter.start<end: #overlapping
            end=max(inter.end,end)
        else: #no-overlapping
            mergedIntervals.append(Interval(start,end))
            start=inter.start
            end=inter.end
    mergedIntervals.append(Interval(start,end)) #the last one
    return mergedIntervals

def main():
    for i in solution([Interval(1,4),Interval(4,5),Interval(5,9)]):
        i.print_interval()
    print()
    
    for i in solution([Interval(6,10),Interval(2,7),Interval(5,7)]):
        i.print_interval()
    print()

    for i in solution([Interval(7,13),Interval(2,4),Interval(5,6)]):
        i.print_interval()
    print()
    
main()

