class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        ans = []
        for i in range(len(arr)):
            char = list(arr[i])
            l = 0
            r = len(char) - 1
            while l <= r:
                char[l], char[r] = char[r], char[l]
                l += 1
                r -= 1
            ans.append("".join(char))
        return " ".join(ans)