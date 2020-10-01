#Given a binary tree and a node, find the level order successor of the given node in the tree.
#The level order successor is the node that appears right after the given node in the level order traversal.
from collections import deque
class TreeNode:
    def __init__(self,val):
        self.value=val
        self.left,self.right=None,None
'''Solution1
def Successor(root,key):
    queue=deque()
    base=deque()
    queue.append(root)
    while queue:
        count=len(queue)
        for _ in range(count):
            node=queue.popleft()
            base.append(node.value)
            while len(base)>2:
                base.popleft()
            if base[0]==key and len(base)==2:
                return base[1]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return -1
'''
#Solution2-Educative
def Successor(root,key):
    queue=deque()
    queue.append(root)
    while queue:
        node=queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        if node.value==key:
            return queue[0].value if queue else -1
    return -1

def main():
    root=TreeNode(12)
    root.left=TreeNode(7)
    root.right=TreeNode(1)
    root.left.left=TreeNode(9)
    root.left.right=TreeNode(3)
    root.right.left=TreeNode(10)
    root.right.right=TreeNode(5)
    print(Successor(root,4))

main()