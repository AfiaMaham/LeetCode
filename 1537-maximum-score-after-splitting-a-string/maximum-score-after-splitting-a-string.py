class Solution:
    def maxScore(self, s: str) -> int:
        total = 0
        for i in range(len(s)-1):
            add = s[:i+1].count('0') + s[i+1:].count('1')
            total = max(total,add)
        return total
