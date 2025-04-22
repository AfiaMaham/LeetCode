class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  Kadane’s Algorithm
        if len(prices) < 2:
            return 0
        max_pro = 0
        curr = prices[0]

        for i in range(1, len(prices)):
            pro = prices[i] - curr
            max_pro = max(max_pro, pro)
            curr = min(curr, prices[i])
        return max_pro
