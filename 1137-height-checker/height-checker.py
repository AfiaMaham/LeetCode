class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        sorted = []
        for i in range(len(heights)):
            sorted.append(heights[i])
            
        sorted.sort()
        for i in range(len(heights)):
            if sorted[i] != heights[i]:
                count += 1
        return count
        