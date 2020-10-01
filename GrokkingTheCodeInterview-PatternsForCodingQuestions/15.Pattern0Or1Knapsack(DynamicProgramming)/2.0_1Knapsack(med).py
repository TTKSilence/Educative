#Given two integer arrays to represent weights and profits of 'N' items,
#find a subset of these items which will give us maximum profit
#such that their cumulative weight is not more than a given number 'C'.
#Each item can only be selected once, which means either we put an item in the knapsack or we skip it.
'''Solution1-Basic
def Knapsack(weights,profits,C):
    return KnapsackRecursive(weights,profits,C,0)

def KnapsackRecursive(weights,profits,capacity,index):
    if capacity<=0 or index>=len(profits):
        return 0
    profit1=0
    if weights[index]<=capacity:
        profit1=profits[index]+KnapsackRecursive(weights,profits,capacity-weights[index],index+1)
    profit2=KnapsackRecursive(weights,profits,capacity,index+1)
    return max(profit1,profit2) 
'''

'''Solution2- Top-down DP with memoization
def Knapsack(weights,profits,capacity):
    dp=[[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return KnapsackRecursive(weights,profits,capacity,0,dp)

def KnapsackRecursive(weights,profits,capacity,currentindex,dp):
    if capacity<=0 or currentindex>=len(profits):
        return 0
    if dp[currentindex][capacity]!=-1:
        return dp[currentindex][capacity]
    profit1=0
    if weights[currentindex]<=capacity:
        profit1=profits[currentindex]\
            +KnapsackRecursive(weights,profits,capacity-weights[currentindex],currentindex+1,dp)
    profit2=KnapsackRecursive(weights,profits,capacity,currentindex+1,dp)
    dp[currentindex][capacity]=max(profit1,profit2)
    return dp[currentindex][capacity]
'''

'''Solution3- Bottom-up DP with memoization
def Knapsack(weights,profits,capacity):
    n=len(profits)
    if capacity<=0 or len(weights)!=n:
        return 0
    dp=[[0 for x in range(capacity+1)] for y in range(n)]
    for i in range(0,n):
        dp[i][0]=0
    for c in range(0,capacity+1):
        if weights[0]<=c:
            dp[0][c]=profits[0]
    for i in range(1,n):
        for c in range(1,capacity+1):
            profit1,profit2=0,0
            if weights[i]<=c:
                profit1=profits[i]+dp[i-1][c-weights[i]]
            profit2=dp[i-1][c]
            dp[i][c]=max(profit1,profit2)
    return dp[n-1][capacity]
'''

'''Solution3- Bottom-up DP with memoization-Improvement'''
def Knapsack(weights,profits,capacity):
    n=len(profits)
    if capacity<=0 or len(weights)!=n:
        return 0
    dp=[[0 for x in range(capacity+1)] for y in range(2)]
    
    for c in range(0,capacity+1):
        if weights[0]<=c:
            dp[0][c]=dp[1][c]=profits[0]

    for i in range(1,n):
        for c in range(0,capacity+1):
            profit1,profit2=0,0
            if weights[i]<=c:
                profit1=profits[i]+dp[(i-1)%2][c-weights[i]]
            profit2=dp[(i-1)%2][c]
            dp[i%2][c]=max(profit1,profit2)
    return dp[(n-1)%2][capacity]


'''Solution- print the set of items included in the knapsack.
def Knapsack(weights,profits,capacity):
    n=len(profits)
    if capacity<=0 or len(weights)!=n:
        return 0
    dp=[[0 for x in range(capacity+1)] for y in range(n)]
    for i in range(0,n):
        dp[i][0]=0
    for c in range(0,capacity+1):
        if weights[0]<=c:
            dp[0][c]=profits[0]
    for i in range(1,n):
        for c in range(1,capacity+1):
            profit1,profit2=0,0
            if weights[i]<=c:
                profit1=profits[i]+dp[i-1][c-weights[i]]
            profit2=dp[i-1][c]
            dp[i][c]=max(profit1,profit2)
    print_items(dp,weights,profits,capacity)
    return dp[n-1][capacity]

def print_items(dp,weights,profits,capacity):
    print('The selected items are:',end='')
    n=len(weights)
    totalprofits=dp[n-1][capacity]
    for i in range(n-1,0,-1):
        if totalprofits!=dp[i-1][capacity]:
            print(str(weights[i])+' ',end='')
            capacity-=weights[i]
            totalprofits-=profits[i]
    if totalprofits!=0:
        print(str(weights[0]+' ',end=''))
    print()
'''


def main():
    weights=[1,3,5,2]
    profits=[1,10,16,6]
    print(Knapsack(weights,profits,7))
    print(Knapsack(weights,profits,6))

main()
