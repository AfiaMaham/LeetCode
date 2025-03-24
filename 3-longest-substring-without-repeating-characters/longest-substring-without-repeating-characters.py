class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str1 = ""
        sum = 0
        count = 0
        for i in range(len(s)):
            if s[i] in str1:
                if count > sum:
                    sum = count
                ind = str1.index(s[i])
                print(ind)
                str1 = str1[ind+1:]
                count = len(str1)
            str1 += s[i]
            count += 1
       
        return max(count,sum)

