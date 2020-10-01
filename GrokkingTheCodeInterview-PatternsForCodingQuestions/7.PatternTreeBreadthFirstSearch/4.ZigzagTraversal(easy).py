#Given a binary tree, populate an array to represent its zigzag level order traversal.
#You should populate the values of all nodes of the first level from left to right,
#then right to left for the next level and keep alternating in the same manner for the following levels.
from collections import deque
class TreeNode:
    def __init__(self,val):
        self.value=val
        self.left,self.right=None,None

def ZigzagTraversal(root):
    queue=deque()
    ans=[]
    queue.append(root)
    tag=False
    while queue:
        temp=[]
        count=len(queue)
        for _ in range(count):
            node=queue.popleft()
            temp.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if tag:
            temp.reverse()
        ans.append(temp)
        tag=not tag
    return ans

def main():
    root=TreeNode(12)
    root.left=TreeNode(7)
    root.right=TreeNode(1)
    root.left.left=TreeNode(9)
    root.left.right=TreeNode(3)
    root.right.left=TreeNode(10)
    root.right.right=TreeNode(5)
    print(ZigzagTraversal(root))

main()

