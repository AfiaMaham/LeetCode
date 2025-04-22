class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = l + 1
        while True:
            if nums[l] + nums[r] == target:
                return [l, r]
            if r == len(nums) - 1:
                l += 1
                r = l + 1
            else:
                r += 1
                