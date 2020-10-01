#Given a set of numbers that might contain duplicates, find all of its distinct subsets.
def subsets(array):
    subsets=[[]]
    array.sort()
    for i in range(len(array)):
        if i>0 and array[i]==array[i-1]:
            start=count
        else:
            start=0
        count=len(subsets)
        for j in range(start,count):
            subsets.append(subsets[j]+[array[i]])
    return subsets

def main():
    print(subsets([1,3,3]))
    print(subsets([1,5,3,3]))

main()