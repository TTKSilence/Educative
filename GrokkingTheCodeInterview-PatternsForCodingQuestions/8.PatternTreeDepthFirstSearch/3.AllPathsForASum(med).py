#Given a binary tree and a number 'S',
#find all paths from root-to-leaf such that the sum of all the node values of each path equals 'S'.
class TreeNode:
    def __init__(self,val):
        self.value=val
        self.left,self.right=None,None

def AllPaths(root,S):
    allp=[]
    curp=[]
    OnePath(root,S,curp,allp)
    return allp

def OnePath(node,sum,curp,allp):
    if not node:
        return
    curp.append(node.value)
    if sum==node.value and not node.left and not node.right:
        allp.append(list(curp))
    else:
        OnePath(node.left,sum-node.value,curp,allp)
        OnePath(node.right,sum-node.value,curp,allp)
    curp.pop()

def main():
    root=TreeNode(12)
    root.left=TreeNode(7)
    root.right=TreeNode(1)
    root.left.left=TreeNode(4)
    root.right.left=TreeNode(10)
    root.right.right=TreeNode(5)
    print(AllPaths(root,23))
    print(AllPaths(root,16))

main()
