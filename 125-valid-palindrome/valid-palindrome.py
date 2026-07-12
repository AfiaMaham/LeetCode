class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''

        for i in range(len(s)):
            if s[i].isalnum():
                string += s[i].lower()
        
        right = len(string) -1
        reverse = ''
        for i in range(len(string)):
            reverse += string[right]
            right -= 1
        
        if string == reverse:
            return True
        return False
        