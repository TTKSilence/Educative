#Any number will be called a happy number if, 
#after repeatedlly replacing it with a number equal to the sum of the square of all of its digits, 
#leads us to number '1'. All other (nor-happy) numbers will never reach '1'.
#Instead, they will be stuck in a cycle of numbers which does not include '1'.

def solution(num):
    '''Solution1
    nums=[]
    while num not in nums:
        if num==1:
            return True
        nums.append(num)
        sum=0
        while num//10!=0 or num%10!=0:
            sum+=(num%10)*(num%10)
            num=num//10
        num=sum
    return False
    '''

#Solution2_Educative
    slow=num
    fast=SquareSum(num)
    while fast!=slow:
        fast=SquareSum(SquareSum(fast))
        slow=SquareSum(slow)
    return slow==1

def SquareSum(num):
    sum=0
    while num//10!=0 or num%10!=0:
        sum+=(num%10)*(num%10)
        num=num//10
    return sum
    

def main():
    print(solution(23))
    print(solution(12))

main()

            