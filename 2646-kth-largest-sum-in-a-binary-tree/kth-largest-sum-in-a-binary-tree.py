from collections import deque
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            level = 0
            for i in range(len(q)):
                node = q.popleft()  
                if node:
                    level += node.val
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        res.sort()
        if k <= len(res):
            return res[-k]
        else:
            return -1

        
            