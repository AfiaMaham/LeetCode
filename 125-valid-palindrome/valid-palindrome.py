class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        reverse = ''
        for i in range(len(s)):
            if s[i].isalnum():
                string += s[i].lower()
                reverse = s[i].lower() + reverse
        
        if string == reverse:
            return True
        return False
        