from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [0]*9
        cols = [0]*9
        boxes = [0]*9
        empties = []
        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == '.':
                    empties.append((i, j))
                else:
                    d = int(ch)
                    bit = 1 << (d - 1)
                    rows[i] |= bit
                    cols[j] |= bit
                    boxes[(i // 3) * 3 + j // 3] |= bit
        full = (1 << 9) - 1

        def solve():
            if not empties:
                return True
            best_idx = -1
            best_mask = 0
            best_count = 10
            for idx, (i, j) in enumerate(empties):
                b = (i // 3) * 3 + j // 3
                mask = ~(rows[i] | cols[j] | boxes[b]) & full
                cnt = mask.bit_count()
                if cnt < best_count:
                    best_count = cnt
                    best_mask = mask
                    best_idx = idx
                    if cnt == 1:
                        break
            if best_count == 0:
                return False
            i, j = empties.pop(best_idx)
            b = (i // 3) * 3 + j // 3
            mask = best_mask
            while mask:
                bit = mask & -mask
                mask -= bit
                d = bit.bit_length()
                board[i][j] = str(d)
                rows[i] |= bit
                cols[j] |= bit
                boxes[b] |= bit
                if solve():
                    return True
                rows[i] ^= bit
                cols[j] ^= bit
                boxes[b] ^= bit
                board[i][j] = '.'
            empties.insert(best_idx, (i, j))
            return False

        solve()
