#Given a binary tree, find the length of its diameter.
#The diameter of a tree is the number of nodes on the longest path between any two leaf nodes.
#The diameter of a tree may or may not pass through the root.
class TreeNode:
    def __init__(self,val):
        self.value=val
        self.left,self.right=None,None

class FindTreeDiameter:
    def __init__(self):
        self.treediameter=0

    def find(self,root):
        self.radius(root)
        return self.treediameter

    def radius(self,node):
        if not node:
            return 0
        leftradius=self.radius(node.left)
        rightradius=self.radius(node.right)
        diameter=leftradius+rightradius+1
        
        self.treediameter=max(diameter,self.treediameter)
    
        return max(leftradius,rightradius)+1

def main():
    TreeDiameter=FindTreeDiameter()
    root=None
    print(TreeDiameter.find(root))
    
    root=TreeNode(1)
    print(TreeDiameter.find(root))
    
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.left=TreeNode(4)
    root.right.left=TreeNode(5)
    root.right.right=TreeNode(6)
    print(TreeDiameter.find(root))

    root.right.left.left=TreeNode(7)
    root.right.left.right=TreeNode(8)
    root.right.left.right.left=TreeNode(10)
    root.right.right.right=TreeNode(9)
    root.right.right.right.left=TreeNode(11)
    print(TreeDiameter.find(root))

main()


