class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        L = 0
        R = len(matrix) - 1

        row = -1

        while L <= R: 
            M = L + (R - L)//2

            if matrix[M][0] > target: 
                R = M - 1
            elif matrix[M][len(matrix[M]) - 1] < target:
                L = M + 1
            else:
                row = M
                break

        if row == -1: return False


        l = 0
        r = len(matrix[row]) - 1

        while l <= r: 
            m = l + (r - l)//2

            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else: 
                return True
        
        return False



            

        