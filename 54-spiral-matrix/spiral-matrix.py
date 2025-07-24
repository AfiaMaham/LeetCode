class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spiral(matrix, m, n, result, r, c, dr, dc):
            if (m == 0 or n == 0):
                return
            
            for i in range(n):
                r = r + dr
                c = c + dc
                result.append(matrix[r][c])

            spiral(matrix, n, m - 1, result, r, c, dc, -dr)

        result = []
        m = len(matrix)
        n = len(matrix[0])
        spiral(matrix, m, n, result, 0, -1, 0, 1)
        return result