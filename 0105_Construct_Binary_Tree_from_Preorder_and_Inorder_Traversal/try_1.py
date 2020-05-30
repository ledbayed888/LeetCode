# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        v = preorder.pop(0)
        root = TreeNode(v)
        inorder_index = inorder.index(v)
        
        root.left = self.buildTree(preorder, inorder[:inorder_index])
        root.right = self.buildTree(preorder, inorder[inorder_index+1:])
        
        return root
