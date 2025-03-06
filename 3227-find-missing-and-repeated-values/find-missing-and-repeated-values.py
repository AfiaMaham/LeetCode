class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        list1 = []
        ans = []
        for i in grid:
            for j in i:
                if j in list1:
                    ans.append(j)
                list1.append(j)
        list1.sort()
        for i in range(len(list1)-1):
            if list1[i+1] - list1[i] == 2:
                ans.append(list1[i]+1)
                return ans
        if list1[0] > 1:
            ans.append(list1[0] - 1)
            return ans
        ans.append(list1[-1]+1)
        return ans
