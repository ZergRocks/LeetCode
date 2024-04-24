class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []

        m, n = len(mat), len(mat[0])
        result = []

        # 각 대각선 방향에 대한 델타 값
        directions = [(-1, 1), (1, -1)]
        row, col = 0, 0
        direction = 0

        for _ in range(m * n):
            result.append(mat[row][col])

            # 다음 요소의 좌표 계산
            row += directions[direction][0]
            col += directions[direction][1]

            # 다음 요소가 행렬의 경계를 벗어나는 경우 방향 전환
            if row >= m:
                row = m - 1
                col += 2
                direction = 1 - direction
            elif col >= n:
                col = n - 1
                row += 2
                direction = 1 - direction
            elif row < 0:
                row = 0
                direction = 1 - direction
            elif col < 0:
                col = 0
                direction = 1 - direction

        return result