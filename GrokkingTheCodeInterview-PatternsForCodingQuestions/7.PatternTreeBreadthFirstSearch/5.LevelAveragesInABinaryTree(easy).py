#Given a binary tree, populate an array to represent the averages of all of its levels.
from collections import deque
class TreeNode:
    def __init__(self,val):
        self.value=val
        self.left,self.right=None,None

def LevelAverage(root):
    queue=deque()
    ans=[]
    queue.append(root)
    while queue:
        temp=0
        count=len(queue)
        for _ in range(count):
            node=queue.popleft()
            temp+=node.value
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(temp/count)
    return ans

def main():
    root=TreeNode(12)
    root.left=TreeNode(7)
    root.right=TreeNode(1)
    root.left.left=TreeNode(9)
    root.left.right=TreeNode(3)
    root.right.left=TreeNode(10)
    root.right.right=TreeNode(5)
    print(LevelAverage(root))

main()
