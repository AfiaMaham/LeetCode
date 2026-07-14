class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarySearch(left, right):
            if left >= right:
                if target > nums[left]:
                    return left+1
                else:
                    return left
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(left, mid - 1)
            else:
                return binarySearch(mid + 1, right)

        return binarySearch(0, len(nums) - 1)
        