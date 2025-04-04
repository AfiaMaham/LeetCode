class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        diff = 0
        if len(nums) == 1:
            return 0
        nums.sort()
        for i in range(len(nums)-1):
            d = abs(nums[i] - nums[i+1])
            if diff < d:
                diff = d
        return diff