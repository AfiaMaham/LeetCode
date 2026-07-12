class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        startingIndex = 0
        sub = s[startingIndex : k]
        count = 0
        for i in sub:
            if i in 'aeiou':
                count += 1
        max = count
 
        for i in range(k, len(s)):
            if s[i] in 'aeiou':
                count += 1
            if sub[0] in 'aeiou':
                count -= 1
            startingIndex += 1
            sub = s[startingIndex: i+1] 
        
            if count > max:
                max = count

        return max

        