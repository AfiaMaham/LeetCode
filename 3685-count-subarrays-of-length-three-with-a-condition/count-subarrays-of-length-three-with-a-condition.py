class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        l = 0
        r = 3

        while r != len(nums)+1:
            sub = nums[l:r]
            print(sub)
            if sub[0] + sub[2] == sub[1]/2:
                count += 1
            l += 1
            r += 1
        return count