class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        directions = [
            (-1, 1), # up
            (1, -1)  # down
        ]
        row, col = 0, 0
        is_going_up = False

        for _ in range(m * n):
            result.append(mat[row][col])
            row += directions[is_going_up][0]
            col += directions[is_going_up][1]

            if row >= m:
                row = m - 1
                col += 2
                is_going_up = not is_going_up
            elif col >= n:
                col = n - 1
                row += 2
                is_going_up = not is_going_up
            elif row < 0:
                row = 0
                is_going_up = not is_going_up
            elif col < 0:
                col = 0
                is_going_up = not is_going_up
            
        return result