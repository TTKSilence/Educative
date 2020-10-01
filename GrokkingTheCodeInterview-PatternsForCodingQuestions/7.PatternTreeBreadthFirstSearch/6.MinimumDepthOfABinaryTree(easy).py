#Find the minimum depth of a binary tree.
#The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node
from collections import deque
class TreeNode:
    def __init__(self,val):
        self.value=val
        self.left,self.right=None,None

def MinDepth(root):
    queue=deque()
    depth=0
    queue.append(root)
    while queue:
        depth+=1
        count=len(queue)
        for _ in range(count):
            node=queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
    return depth

def main():
    root=TreeNode(12)
    root.left=TreeNode(7)
    root.right=TreeNode(1)
    root.left.left=TreeNode(9)
    root.left.right=TreeNode(3)
    #root.right.left=TreeNode(10)
    #root.right.right=TreeNode(5)
    print(MinDepth(root))

main()