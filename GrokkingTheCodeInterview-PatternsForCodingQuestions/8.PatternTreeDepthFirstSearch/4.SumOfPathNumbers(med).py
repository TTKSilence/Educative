#Given a binary tree where each node can only have a digit (0-9) value,
#each root-to-leaf path will represent a number.
#Find the total sum of all the numbers represented by all paths.
class TreeNode:
    def __init__(self,val):
        self.value=val
        self.left,self.right=None,None
'''Solution1
def SumPN(root):
    ans=[]
    Sum(root,0,ans)
    res=0
    for i in ans:
        res+=i
    return res

def Sum(node,sum,ans):
    if not node:
        return
    sum=10*sum+node.value
    if not node.left and not node.right:
        ans.append(int(sum))
    else:
        Sum(node.left,sum,ans)
        Sum(node.right,sum,ans)
'''
#Solution2-Educative
def SumPN(root):
    return Sum(root,0)

def Sum(node,sum):
    if not node:
        return 0
    sum=10*sum+node.value
    if not node.left and not node.right:
        return sum
    return Sum(node.left,sum)+Sum(node.right,sum)  

def main():
    root=TreeNode(1)
    root.left=TreeNode(7)
    root.right=TreeNode(9)
    root.left.left=TreeNode(4)
    root.right.left=TreeNode(2)
    root.right.right=TreeNode(5)
    print(SumPN(root))

main()
    
