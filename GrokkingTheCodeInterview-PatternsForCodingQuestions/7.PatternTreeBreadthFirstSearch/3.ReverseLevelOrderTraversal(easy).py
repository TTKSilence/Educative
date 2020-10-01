#Given a binary tree, populate an array to represent its level-by-level traversal in reverse order.
#(lowest level comes first)
#The values of all nodes in each level from left to right in separate sub-arrays should be populated.
from collections import deque

class TreeNode:
    def __init__(self,val):
        self.value=val
        self.left,self.right=None,None

def ReverseOrderTraversal(root):
    queue=deque()
    ans=deque()
    queue.append(root)
    while queue:
        count=len(queue)
        temp=[]
        for _ in range(count):
            node=queue.popleft()
            temp.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.appendleft(temp)
    return ans

def main():
    root=TreeNode(12)
    root.left=TreeNode(7)
    root.right=TreeNode(1)
    root.left.left=TreeNode(9)
    root.left.right=TreeNode(3)
    root.right.left=TreeNode(10)
    root.right.right=TreeNode(5)
    print(ReverseOrderTraversal(root))

main()
