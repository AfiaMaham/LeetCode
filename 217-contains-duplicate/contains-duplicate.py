class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set1 = set(nums)
        # if len(set1) != len(nums):
        #     return True
        # return False
        set1 = set()
        for i in range(len(nums)):
            if nums[i] in set1:
                return True
            set1.add(nums[i])
        return False