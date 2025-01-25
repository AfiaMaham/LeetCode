class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = ''
        for x in s:
            if x.isalnum():
                str += x.lower()
        if str == str[::-1]:
            return True
        else:
            return False