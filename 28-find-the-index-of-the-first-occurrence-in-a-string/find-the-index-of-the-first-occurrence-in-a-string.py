class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0
        r = len(needle)
        while r <= len(haystack):
            sub = haystack[l:r]
            if sub != needle:
                l += 1
                r = len(needle) + l
            else:
                return l
        return -1