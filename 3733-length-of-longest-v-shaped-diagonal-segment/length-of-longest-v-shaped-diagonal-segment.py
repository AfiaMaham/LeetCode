from typing import List
from array import array

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  
        clockwise = {0: 1, 1: 2, 2: 3, 3: 0}
        orders = [
            (range(n-1, -1, -1), range(m-1, -1, -1)),  
            (range(n-1, -1, -1), range(m)),            
            (range(n), range(m)),                     
            (range(n), range(m-1, -1, -1)),           
        ]

        def alloc():
            return [array('H', [0]) * m for _ in range(n)]

        nt0 = [None] * 4
        nt1 = [None] * 4
        nt2 = [None] * 4

        def compute_no_turn(d: int):
            if nt0[d] is not None:
                return
            a0, a1, a2 = alloc(), alloc(), alloc()
            di, dj = dirs[d]
            ri, rj = orders[d]
            for i in ri:
                for j in rj:
                    ni, nj = i + di, j + dj
                    if grid[i][j] == 1:
                        a0[i][j] = 1 + (a1[ni][nj] if 0 <= ni < n and 0 <= nj < m else 0)
                    if grid[i][j] == 2:
                        a1[i][j] = 1 + (a2[ni][nj] if 0 <= ni < n and 0 <= nj < m else 0)
                    if grid[i][j] == 0:
                        a2[i][j] = 1 + (a1[ni][nj] if 0 <= ni < n and 0 <= nj < m else 0)
            nt0[d], nt1[d], nt2[d] = a0, a1, a2

        ans = 0

        for d in range(4):
            td = clockwise[d]
            compute_no_turn(d)
            compute_no_turn(td)

            bt0, bt1, bt2 = alloc(), alloc(), alloc()
            di, dj = dirs[d]
            tdi, tdj = dirs[td]
            ri, rj = orders[d]

            a0_d, a1_d, a2_d = nt0[d], nt1[d], nt2[d]       
            a1_td, a2_td = nt1[td], nt2[td]

            for i in ri:
                for j in rj:
                    ni, nj = i + di, j + dj
                    ti, tj = i + tdi, j + tdj

                    if grid[i][j] == 1:
                        best = 1
                        if 0 <= ni < n and 0 <= nj < m:
                            best = max(best, 1 + bt1[ni][nj])       
                        if 0 <= ti < n and 0 <= tj < m:
                            best = max(best, 1 + a1_td[ti][tj])     
                        bt0[i][j] = best
                        if best > ans:
                            ans = best
                    if grid[i][j] == 2:
                        best = 1
                        if 0 <= ni < n and 0 <= nj < m:
                            best = max(best, 1 + bt2[ni][nj])       
                        if 0 <= ti < n and 0 <= tj < m:
                            best = max(best, 1 + a2_td[ti][tj])    
                        bt1[i][j] = best
                    if grid[i][j] == 0:
                        best = 1
                        if 0 <= ni < n and 0 <= nj < m:
                            best = max(best, 1 + bt1[ni][nj])       
                        if 0 <= ti < n and 0 <= tj < m:
                            best = max(best, 1 + a1_td[ti][tj])     
                        bt2[i][j] = best

        return ans
