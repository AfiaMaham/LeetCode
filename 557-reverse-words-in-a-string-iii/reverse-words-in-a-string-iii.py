class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        ansArray = []
        for i in arr:
            ansArray.append(i[::-1])
        s = " ".join(ansArray)
        return s