class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = []
        ans = ""
        w = ""
        for i in range(len(s)):
            w += s[i]
            if len(w) == (2*k):
                arr.append(w)
                w = ""
            elif (len(w) < k or len(w) < (2*k)) and i == (len(s) - 1):
                arr.append(w)

        for i in arr:
            char = list(i)
            l = 0
            r = k - 1
            if len(i) == (2*k) or (len(i) < (2*k) and len(i) >= k):
                while l < r:
                    char[l], char[r] = char[r], char[l]
                    l += 1
                    r -= 1
                ans += "".join(char)
            elif len(i) < k:
                l = 0
                r = len(i) - 1
                while l < r:
                    char[l], char[r] = char[r], char[l]
                    l += 1
                    r -= 1
                ans += "".join(char)
                
        return ans



