class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            else:
                count += 1
        return len(nums) - count
        


