from typing import List

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        powers = [1]
        LIMIT = 10**9
        while powers[-1] <= LIMIT:
            powers.append(powers[-1] * 4)

        ans = 0
        for l, r in queries:
            total = 0
            for k in range(len(powers) - 1):
                left = max(l, powers[k])
                right = min(r, powers[k + 1] - 1)
                if left <= right:
                    total += (right - left + 1) * (k + 1)
            ans += (total + 1) // 2
        return ans
