#2025-10-16 time: 12:03
class Solution(object):
    def minimumOperations(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        steps = 0
        
        for col in range(len(grid[0])):
            for row in range(len(grid)-1):
                if grid[row][col]>=grid[row+1][col]:
                    steps += grid[row][col]-grid[row+1][col]+1
                    grid[row+1][col] = grid[row][col]+1
        return steps