from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        for i in range(n):
            for j in range(n):
                if points[i][0] <= points[j][0] and points[i][1] >= points[j][1] and (points[i][0] < points[j][0] or points[i][1] > points[j][1]):
                    valid = True
                    for k in range(n):
                        if k != i and k != j:
                            if points[i][0] <= points[k][0] <= points[j][0] and points[j][1] <= points[k][1] <= points[i][1]:
                                valid = False
                                break
                    if valid:
                        ans += 1
        return ans
