import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        p = 1
        for i in range(len(nums)):
            if i != 0:
                p *= nums[i-1]
            ans.append(p)
        
        nums.reverse()
        ans.reverse()
        p = 1
        for i in range(len(nums)):
            if i != 0:
                p *= nums[i-1]
            ans[i] = ans[i] * p

        ans.reverse()
        return ans



        