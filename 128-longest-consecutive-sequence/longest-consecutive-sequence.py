class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = []
        arrCopy = []
        nums.sort()
        if len(nums) == 0:
            return 0
        arr.append(nums[0])
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                arr.append(nums[i+1])
            elif nums[i+1] == nums[i]:
                continue
            else:
                if len(arrCopy) < len(arr):
                    arrCopy = arr.copy()
                arr.clear()
                arr.append(nums[i])
        if len(arrCopy) < len(arr):
             arrCopy = arr.copy()
        return len(arrCopy)

