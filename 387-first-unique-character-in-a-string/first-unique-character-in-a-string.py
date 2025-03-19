from collections import deque
class Solution:
    def firstUniqChar(self, s: str) -> int:
        q = deque(s)
        new = ""
        for i in range(len(s)):
            char = q.popleft()
            if char not in q and char not in new:
                return i
            new += char

        return -1