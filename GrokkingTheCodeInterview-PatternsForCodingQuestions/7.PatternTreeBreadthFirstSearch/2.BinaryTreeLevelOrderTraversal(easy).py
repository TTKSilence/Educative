#Given a binary tree, populate an array to represent its level-by-level traversal.
#The values of all nodes of each level from left to right in separate sub-arrays should be populated.
class TreeNode:
    def __init__(self,val):
        self.value=val
        self.left,self.right=None,None

def traverse(root):
    deque=[root]
    ans=[]
    while deque:
        temp=[]
        count=len(deque)  #The key line!
        for _ in range(count):
            node=deque.pop(0)
            temp.append(node.value)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        ans.append(temp)
    return ans

def main():
    root=TreeNode(12)
    root.left=TreeNode(7)
    root.right=TreeNode(1)
    root.left.left=TreeNode(9)
    root.left.right=TreeNode(3)
    root.right.left=TreeNode(10)
    root.right.right=TreeNode(5)
    print(traverse(root))

main()


