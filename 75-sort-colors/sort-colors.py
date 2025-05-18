class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        list1 = []
        list2 = []
        list3 = []
        for i in range(len(nums)):
            if nums[i] == 0:
                list1.append(0)
            elif nums[i] == 1:
                list2.append(1)
            else:
                list3.append(2)
        nums.clear()
        list4 = list1+list2+list3
        for i in list4:
            nums.append(i)
        
        