class Solution:
    def isPalindrome(self, x: int) -> bool:
        str1 = str(x)
        if str1 == str1[::-1]:
            return True
        return False