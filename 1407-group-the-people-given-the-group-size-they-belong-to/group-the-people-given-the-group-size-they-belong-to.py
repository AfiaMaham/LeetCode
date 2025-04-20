class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dict = {}
        ans = []
        for ind, val in enumerate(groupSizes):
            if val not in dict:
                dict[val] = [ind]
            else:
                if len(dict[val]) == val:
                    ans.append(dict[val])
                    dict[val] = []
     
                dict[val].append(ind)
        
        for key, val in dict.items():
            ans.append(val)
        return ans
        