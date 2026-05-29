class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        best = 0
        y = len(grid)
        x = len(grid[0])
        visited = set()

        def backTrack(row, col):
            print(row, col)
            if row >= 0 and row < y and col >= 0 and col < x and (row, col) not in visited and grid[row][col] == 1:
                visited.add((row, col))
                return 1 + (backTrack(row-1, col) + backTrack(row+1, col) + backTrack(row, col-1) + backTrack(row, col+1))
            else:
                return 0
            
            
        for row in range(0, y):
            for col in range(0, x):
                if grid[row][col] == 1 and (row, col) not in visited:
                    print(row)
                    new = backTrack(row, col)
                    print(new)
                    best = max(best, new)
        
        return best
