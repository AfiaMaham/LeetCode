class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result = 101
        countW = sum([(1 if blocks[i] == 'W' else 0) for i in range(k-1)])

        for i in range(k-1,len(blocks)):
            countW += (blocks[i] == 'W')
            result = min(result,countW)
            countW -= (blocks[i-k+1] == 'W')
        return result