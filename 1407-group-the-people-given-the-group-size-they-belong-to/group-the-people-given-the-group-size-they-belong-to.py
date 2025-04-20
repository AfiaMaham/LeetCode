class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dict = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in dict:
                dict[groupSizes[i]] = [i]
            else:
                dict[groupSizes[i]].append(i)
        
        ans = []
        
        for key, val in dict.items():
            l = 0
            k = key
            if key != len(val):
                for i in range(len(val)//key):
                    ans.append(val[l:k])
                    l = k
                    k += key
            else:
                ans.append(val)
        return ans