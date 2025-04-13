class Solution:
    def hammingWeight(self, n: int) -> int:
        bit = bin(n)
        split = bit[2:]
        counting = split.count('1')
        return counting