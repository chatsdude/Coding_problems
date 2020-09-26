'''In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins'''

def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        res=[]
        def DFS(root,parent,depth):
            if not root:
                return 
            if root.val==x or root.val==y:
                res.append((parent,depth))
            if root.left:
                DFS(root.left,root,depth+1)
            if root.right:
                DFS(root.right,root,depth+1)
        DFS(root,None,0)
        x,y=res
        return x[0]!=y[0] and x[1]==y[1]
            