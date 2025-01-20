class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        length = len(arr[-1])
        return length