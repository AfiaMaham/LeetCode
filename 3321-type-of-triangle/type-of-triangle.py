class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if (nums[0]+nums[1])>nums[2] and (nums[1]+nums[2])>nums[0] and (nums[0]+nums[2])>nums[1]:
            set1 = set(nums)
            if(len(set1) == 1):
                return "equilateral"
            elif(len(set1) == 2):
                return "isosceles"
            elif(len(set1) == len(nums)):
                return "scalene"
        else:
            return "none"