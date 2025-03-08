class Solution:
    sum1 = 0
    sumArr = []
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        elif not root.left and not root.right:
            pre = self.sum1
            self.sum1 += root.val
            if self.sum1 == targetSum:
                return True
            else:               
                self.sum1 = pre
                return False
        elif not root.left:
            self.sum1 += root.val

            return self.hasPathSum(root.right,targetSum)
        elif not root.right:
            self.sum1 += root.val
            return self.hasPathSum(root.left,targetSum)
        else:
            self.sum1 += root.val
            self.sumArr.append(self.sum1)
            if self.hasPathSum(root.left,targetSum):
                return True
            self.sum1 = self.sumArr.pop()
            if self.hasPathSum(root.right,targetSum):
                return True
        return False
        
