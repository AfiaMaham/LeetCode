class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        sub = s[:k]
        vow = "aeiou"
        sum = 0
        t = 0
        print(sub)
        for i in sub:
            if i in vow:
                sum += 1
        t = sum
        for i in range(len(s)-k):
            if sub[0] in vow:
                t -= 1
            if s[k] in vow:
                t += 1
            sum = max(sum,t)
            s = s[1:]
            sub = s[:k]
        return sum
