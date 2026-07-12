class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [0] * len(nums)
        for i in range(len(nums)):
            prefixSum[i] = prefixSum[i-1] + nums[i]

        for i in range(len(nums)):
            pivot = i
            if pivot == 0:
                leftSum = 0
            else:
                leftSum = prefixSum[pivot-1]
            rightSum = prefixSum[-1] - prefixSum[pivot]
            if leftSum == rightSum:
                return pivot
        return -1