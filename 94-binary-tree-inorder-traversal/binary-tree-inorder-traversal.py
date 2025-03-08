# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def Inorder(node):
            if node is None:
                return None
            Inorder(node.left)
            arr.append(node.val)
            Inorder(node.right)

        Inorder(root)
        return arr
        