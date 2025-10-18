#2025-10-18 time: 5:00
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0
        r = (ROWS*COLS)-1

        while l <= r:
            mid = l+(r-l)//2

            row,col = mid//COLS,mid%COLS

            if matrix[row][col]>target:
                r-=1
            elif matrix[row][col]<target:
                l+=1
            else:
                return True

        return False