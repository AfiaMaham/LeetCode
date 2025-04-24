class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            s = curr + nums[i]
            curr = max(s, nums[i])
            maxi = max(curr, maxi)
        return maxi