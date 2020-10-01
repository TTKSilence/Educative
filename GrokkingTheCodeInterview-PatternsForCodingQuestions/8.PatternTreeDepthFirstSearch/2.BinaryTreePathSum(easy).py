#Given a binary tree and a number 'S',
#find if the tree has a path from root-to-leaf 
#such that the sum of all the node values of that path equals 'S'.
class TreeNode:
    def __init__(self,val):
        self.value=val
        self.left,self.right=None,None

def Sum(root,S):
    if not root:
        return False
    if root.value==S and not root.left and not root.right:
        return True
    return Sum(root.left,S-root.value) or Sum(root.right, S-root.value)

def main():
    root=TreeNode(12)
    root.left=TreeNode(7)
    root.right=TreeNode(1)
    root.left.left=TreeNode(9)
    root.right.left=TreeNode(10)
    root.right.right=TreeNode(5)
    print(Sum(root,23))
    print(Sum(root,16))

main()
        

        