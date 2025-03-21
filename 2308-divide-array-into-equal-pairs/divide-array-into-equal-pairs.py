class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)/2
        sum = 0
        count = Counter(nums)
        for i in count:
            sum += (count[i]//2)
        if sum == n:
            return True
        return False
            