class Solution:
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        
        row, col = 0, 0
        direction = 1  
        
        for _ in range(m * n):
            result.append(mat[row][col])
            
            new_row = row - 1 if direction == 1 else row + 1
            new_col = col + 1 if direction == 1 else col - 1
            
            if 0 <= new_row < m and 0 <= new_col < n:
                row, col = new_row, new_col
            else:
                if direction == 1:  
                    if col + 1 < n:  
                        col += 1
                    else:            
                        row += 1
                else: 
                    if row + 1 < m:  
                        row += 1
                    else:            
                        col += 1
                
                direction *= -1
        
        return result
