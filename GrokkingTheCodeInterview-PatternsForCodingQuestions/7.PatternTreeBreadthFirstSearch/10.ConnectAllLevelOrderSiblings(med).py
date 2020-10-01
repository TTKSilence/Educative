#Given a binary tree, connect each node with its level order successor.
#The last node of each level should point to the first node of the next level.
from collections import deque
class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left,self.right,self.next=None,None,None
    def print_level_order(self):
        current=self
        while current:
            print(str(current.value)+"->",end='')
            current=current.next
        print('None')

def AllSiblings(root):
    queue=deque()
    queue.append(root)
    '''Solution1
    sibling=root
    while queue:
        node=queue.popleft()
        sibling.next=node
        sibling=sibling.next
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return root
    '''
    #Solution2-Educative
    prenode,curnode=None,None
    while queue:
        curnode=queue.popleft()
        if prenode:
            prenode.next=curnode
        prenode=curnode
        if curnode.left:
            queue.append(curnode.left)
        if curnode.right:
            queue.append(curnode.right)

def main():
    root=TreeNode(12)
    root.left=TreeNode(7)
    root.right=TreeNode(1)
    root.left.left=TreeNode(9)
    root.left.right=TreeNode(3)
    root.left.right.left=TreeNode(3)
    root.right.left=TreeNode(10)
    root.right.right=TreeNode(5)
    AllSiblings(root)
    root.print_level_order()

main()
