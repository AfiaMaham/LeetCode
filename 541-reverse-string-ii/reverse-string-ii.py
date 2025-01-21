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
            if len(i) == (2*k):
                slice = i[:k]
                print(slice)
                slice1 = slice[::-1]
                print(slice1)
                i = i.replace(slice,slice1)
                print(i)
                ans += i
            elif len(i) < k:
                i = i[::-1]
                ans += i
            elif len(i) < (2*k) and len(i) >= k:
                slice = i[:k]
                slice1 = slice[::-1]
                i = i.replace(slice,slice1)
                ans += i
                
        return ans



