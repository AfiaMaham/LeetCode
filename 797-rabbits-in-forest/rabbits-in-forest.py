class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dict = {}
        ans = []
        for ind, val in enumerate(answers):
            if val == 0:
                ans.append(val)
            else:
                if val not in dict:
                    dict[val] = []
                else:
                    if len(dict[val]) == val:
                        ans.append(val)
                        dict[val] = []
                    else:
                        dict[val].append(ind)
        
        for key, val in dict.items():
            ans.append(key)
        sum1 = sum(ans)
        return sum1 + len(ans)

        