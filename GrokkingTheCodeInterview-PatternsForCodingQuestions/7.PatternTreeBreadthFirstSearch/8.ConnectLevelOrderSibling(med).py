#Given a binary tree, connect each node with its level order successor.
#The last node of each level should point to a null node.
#from __future__ import print_function
from collections import deque
class TreeNode:
    def __init__(self,val):
        self.value=val
        self.left,self.right,self.next=None,None,None
    def print_level_order(self):
        nextLevelRoot=self
        while nextLevelRoot:
            current=nextLevelRoot
            nextLevelRoot=None
            while current:
                print(str(current.value)+"->",end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot=current.left
                    elif current.right:
                        nextLevelRoot=current.right
                current=current.next
            print('None')
'''Solution1
def Sibling(root):
    queue=deque()
    queue.append(root)
    while queue:
        count=len(queue)
        for i in range(count):
            node=queue.popleft()
            if i<count-1:
                node.next=queue[0]
            else:
                node.next=None
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
'''
#Solution2-Educative
def Sibling(root):
    queue=deque()
    queue.append(root)
    while queue:
        pre=None
        count=len(queue)
        for _ in range(count):
            cur=queue.popleft()
            if pre:
                pre.next=cur
            pre=cur
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

def main():
    root=TreeNode(12)
    root.left=TreeNode(7)
    root.right=TreeNode(1)
    root.left.left=TreeNode(9)
    root.left.right=TreeNode(3)
    root.right.left=TreeNode(10)
    root.right.right=TreeNode(5)
    Sibling(root)
    root.print_level_order()

main()