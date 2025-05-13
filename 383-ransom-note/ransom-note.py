class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l = list(magazine)
        print(l)
        for i, char in enumerate (ransomNote):
            if char in l:
                l.remove(char)
            else:
                return False
        return True