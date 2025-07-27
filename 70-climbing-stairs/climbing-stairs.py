class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def helper(k):
            if k <= 2:
                return k
            if k in memo:
                return memo[k]
            memo[k] = helper(k - 1) + helper(k - 2)
            return memo[k]

        return helper(n)
