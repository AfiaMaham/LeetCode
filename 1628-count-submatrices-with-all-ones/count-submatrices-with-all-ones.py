class Solution:
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        ans = 0
        heights = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1

            stack = []
            sum_rectangles = [0] * n

            for j in range(n):
                while stack and heights[stack[-1]] >= heights[j]:
                    stack.pop()

                if stack:
                    prev = stack[-1]
                    sum_rectangles[j] = sum_rectangles[prev] + heights[j] * (j - prev)
                else:
                    sum_rectangles[j] = heights[j] * (j + 1)

                ans += sum_rectangles[j]
                stack.append(j)

        return ans
