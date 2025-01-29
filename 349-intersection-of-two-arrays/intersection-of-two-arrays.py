class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                result.append(nums1[i])
        return result
