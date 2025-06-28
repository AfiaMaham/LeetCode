class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        while len(stones) > 1:
            x = max(stones)
            stones.remove(x)
            y = max(stones)
            stones.remove(y)
            z = abs(x - y)
            if z != 0:
                stones.append(z)
        if len(stones) == 0:
            return 0
        return stones[0]