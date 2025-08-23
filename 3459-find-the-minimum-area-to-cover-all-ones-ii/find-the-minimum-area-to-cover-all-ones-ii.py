from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ones = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1]

        def rect_area(points):
            if not points:
                return float('inf')
            rs = [r for r, _ in points]
            cs = [c for _, c in points]
            return (max(rs) - min(rs) + 1) * (max(cs) - min(cs) + 1)

        ans = float('inf')

        for c1 in range(m):
            for c2 in range(c1 + 1, m):
                g1, g2, g3 = [], [], []
                for r, c in ones:
                    if c <= c1:
                        g1.append((r, c))
                    elif c <= c2:
                        g2.append((r, c))
                    else:
                        g3.append((r, c))
                if g1 and g2 and g3:
                    ans = min(ans, rect_area(g1) + rect_area(g2) + rect_area(g3))

        for r1 in range(n):
            for r2 in range(r1 + 1, n):
                g1, g2, g3 = [], [], []
                for r, c in ones:
                    if r <= r1:
                        g1.append((r, c))
                    elif r <= r2:
                        g2.append((r, c))
                    else:
                        g3.append((r, c))
                if g1 and g2 and g3:
                    ans = min(ans, rect_area(g1) + rect_area(g2) + rect_area(g3))

        for r in range(n - 1):
            for c in range(m - 1):
                g1, g2, g3 = [], [], []
                for x, y in ones:
                    if x <= r and y <= c:
                        g1.append((x, y))
                    elif x <= r and y > c:
                        g2.append((x, y))
                    else:
                        g3.append((x, y))
                if g1 and g2 and g3:
                    ans = min(ans, rect_area(g1) + rect_area(g2) + rect_area(g3))

                g1, g2, g3 = [], [], []
                for x, y in ones:
                    if x <= r:
                        g1.append((x, y))
                    elif y <= c:
                        g2.append((x, y))
                    else:
                        g3.append((x, y))
                if g1 and g2 and g3:
                    ans = min(ans, rect_area(g1) + rect_area(g2) + rect_area(g3))

        for c in range(m - 1):
            for r in range(n - 1):
                g1, g2, g3 = [], [], []
                for x, y in ones:
                    if y <= c and x <= r:
                        g1.append((x, y))
                    elif y <= c and x > r:
                        g2.append((x, y))
                    else:
                        g3.append((x, y))
                if g1 and g2 and g3:
                    ans = min(ans, rect_area(g1) + rect_area(g2) + rect_area(g3))

                g1, g2, g3 = [], [], []
                for x, y in ones:
                    if y <= c:
                        g1.append((x, y))
                    elif x <= r:
                        g2.append((x, y))
                    else:
                        g3.append((x, y))
                if g1 and g2 and g3:
                    ans = min(ans, rect_area(g1) + rect_area(g2) + rect_area(g3))

        return ans if ans != float('inf') else 0
