class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = ""
        for i in s:
            if i.isalnum():
                str1 += i.lower() 
       
        l = 0
        r = len(str1) - 1
        while l < r:
            if str1[l] == str1[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
