class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float('inf')

        while queue:
            row, col = queue.popleft()
            for dr, dc in delta:
                new_row, new_col = row + dr, col + dc
                if (
                    0 <= new_row < m
                ) and (
                    0 <= new_col < n
                ) and (
                    mat[new_row][new_col] > mat[row][col] + 1
                ):
                    mat[new_row][new_col] = mat[row][col] + 1
                    queue.append((new_row, new_col))
        return mat