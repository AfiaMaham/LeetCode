class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        for i in range(len(s)//2):
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1


        