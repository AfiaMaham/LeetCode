class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr = []
        num = ""
        for i in digits:
            num += str(i)
        num = int(num) + 1
        num = str(num)
        for i in num:
            arr.append(int(i))
        return arr

