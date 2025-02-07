class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        char = list(s)
        l = 0
        r = len(char) - 1
        while l < r:
            if char[l] in vowels and char[r] in vowels:
                char[l], char[r] = char[r], char[l]
                l += 1
                r -= 1
            elif char[l] not in vowels:
                l += 1
            elif char[r] not in vowels:
                r -= 1
        return "".join(char)
