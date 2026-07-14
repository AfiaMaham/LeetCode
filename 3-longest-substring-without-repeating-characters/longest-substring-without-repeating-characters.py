class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ''
        maxCount = 0
        count = 0
        for i in range(len(s)):
            if s[i] in sub:
                if count > maxCount:
                    maxCount = count
                l1 = len(sub)
                index = sub.find(s[i])
                sub = sub[index+1:]
                l2 = len(sub)
                count -= (l1 - l2)
            
            sub += s[i]
            count += 1
        
        if count > maxCount:
            maxCount = count
        return maxCount

        