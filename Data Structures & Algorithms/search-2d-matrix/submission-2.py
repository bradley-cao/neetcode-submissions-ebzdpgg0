class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        if matrix[0][0] <= target and matrix[0][cols-1] >= target:
            if target in matrix[0]:
                return True

        for i in range(1, rows):
            if matrix[i][0] > target and matrix[i - 1][0] <= target:
                if target in matrix[i-1]:
                    return True
                return False

        if matrix[rows-1][0] <= target and matrix[rows-1][cols-1] >= target:
            if target in matrix[rows-1]:
                return True

        return False
