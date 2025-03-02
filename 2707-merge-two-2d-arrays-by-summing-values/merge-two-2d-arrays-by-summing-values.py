class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dict = {}
        length = 0
        if len(nums1)> len(nums2):
            length = len(nums1)
        else:
            length = len(nums2)
        for i in range(length):
            if i < len(nums1):
                if nums1[i][0] in dict.keys():
                    dict[nums1[i][0]] += nums1[i][1]
                else:
                    dict.update({nums1[i][0]:nums1[i][1]})
            if i < len(nums2):
                if nums2[i][0] in dict.keys():
                    dict[nums2[i][0]] += nums2[i][1]
                else:
                    dict.update({nums2[i][0]:nums2[i][1]})
        myKeys = list(dict.keys())
        myKeys.sort()

        sd = {i: dict[i] for i in myKeys}
        list1 = []
        for i,j in sd.items():
            list1.append([i,j])
        return list1
