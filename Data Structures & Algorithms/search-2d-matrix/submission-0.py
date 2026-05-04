class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        a, b = m-1, 0
        while m > a >= 0 and n > b >= 0:
            if matrix[a][b] == target:
                return True
            elif matrix[a][b] < target:
                b += 1
            else:
                a -= 1
        return False