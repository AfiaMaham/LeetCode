from collections import deque
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    if node.val not in res:
                        res.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

        res.sort()
        if len(res) < 2:
            return -1
        return res[1]