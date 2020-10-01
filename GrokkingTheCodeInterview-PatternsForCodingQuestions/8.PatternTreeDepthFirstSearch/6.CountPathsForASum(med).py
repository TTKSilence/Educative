#Given a binary tree and a number 'S', 
#find all paths in the tree such that the sum of all the node values of each path equals 'S'.
#Note that the paths can start or end at any node but all paths must follow direction from parent to child.
class TreeNode:
    def __init__(self,val):
        self.value=val
        self.left,self.right=None,None

def CountPaths(root,S):
    return Path(root,S,[])

def Path(node,S,curpath):
    if not node:
        return 0
    curpath.append(node.value)
    count,pathsum=0,0
    for i in range(len(curpath)-1,-1,-1):
        pathsum+=curpath[i]
        if pathsum==S:
            count+=1

    count+=Path(node.left,S,curpath)
    count+=Path(node.right,S,curpath)

    curpath.pop()

    return count

def main():
    root=TreeNode(12)
    root.left=TreeNode(7)
    root.right=TreeNode(1)
    root.left.left=TreeNode(4)
    root.right.left=TreeNode(10)
    root.right.right=TreeNode(5)
    print(CountPaths(root,11))

main()
