#Given a binary tree and a number sequence,
#find if the sequence is present as a root-to-leaf path in the given tree.
class TreeNode:
    def __init__(self,val):
        self.value=val
        self.left,self.right=None,None

def GivenSeq(root,seq):
    if not root:
        return len(seq)==0
    return Path(root,0,seq)

def Path(node,level,seq):
    if not node:
        return False
    if level>=len(seq) or node.value!=seq[level]:
        return False
    if not node.left and not node.right and level==len(seq)-1:
        return True
    return Path(node.left,level+1,seq) or Path(node.right,level+1,seq)


def main():
    root=TreeNode(1)
    root.left=TreeNode(7)
    root.right=TreeNode(9)
    root.left.left=TreeNode(4)
    root.right.left=TreeNode(2)
    root.right.right=TreeNode(5)
    print(GivenSeq(root,[1,7,4]))
    print(GivenSeq(root,[1,9,2]))
    print(GivenSeq(root,[1,7,4,5]))
    print(GivenSeq(root,[1,7]))
    print(GivenSeq(root,[1,7,5]))

main()
    