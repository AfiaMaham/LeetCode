class Solution:
    def coloredCells(self, n: int) -> int:
        val = 1
        for i in range(1, n):
            val += (4 * i)

        return val