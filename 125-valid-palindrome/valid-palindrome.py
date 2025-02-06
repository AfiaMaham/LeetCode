class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = ''
        for x in s:
            if x.isalnum():
                str += x.lower()

        l = 0
        r = len(str) - 1
        while l <= r:
            if str[l] == str[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
