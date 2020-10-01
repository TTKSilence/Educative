#In a non-empty array of integers, every number appears twice except for one, find that single number.
def SingleNumber(array):
    x=array[0]
    for i in array[1:]:
        x=x^i
    return x

def main():
    print(SingleNumber([4,8,5,2,7,8,2,4,7]))
    print(SingleNumber([3,6,6]))

main()