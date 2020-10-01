#Given a set with distinct elements, find all of its distinct subsets.
def subsets(array):
    subsets=[[]]
    for i in array:
        count=len(subsets)
        for j in range(count):
            subsets.append(subsets[j]+[i])
    return subsets

def main():
    print(subsets([1,3]))
    print(subsets([1,5,3]))

main()
