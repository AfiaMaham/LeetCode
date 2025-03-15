class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node):
            if node:
                if node.val == val:
                    return node
                elif val < node.val:
                    return search(node.left)
                else:
                    return search(node.right)
            return None
             
        return search(root)