from typing import List
from bisect import bisect_left
from collections import defaultdict

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        groups = defaultdict(list)
        xs_set = set()
        for idx, (x, y) in enumerate(points):
            groups[x].append((y, idx))
            xs_set.add(x)
        xs = sorted(xs_set)
        for x in xs:
            groups[x].sort(reverse=True)
        ans = 0
        neg_inf = -10**19
        for a_idx, (xA, yA) in enumerate(points):
            pos = bisect_left(xs, xA)
            max_prev = neg_inf
            for xi in range(pos, len(xs)):
                x = xs[xi]
                g = groups[x]
                top = None
                cnt = 0
                for y, idx in g:
                    if idx == a_idx:
                        continue
                    if y <= yA:
                        if top is None or y > top:
                            top = y
                            cnt = 1
                        elif y == top:
                            cnt += 1
                if top is not None:
                    if cnt == 1 and top > max_prev:
                        ans += 1
                    if top > max_prev:
                        max_prev = top
        return ans
