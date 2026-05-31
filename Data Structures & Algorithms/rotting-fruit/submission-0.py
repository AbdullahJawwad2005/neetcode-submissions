from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # okay here we use source based BFS as well
        # first get all rotten fruits and add them to deque
        # then iterate through them and count the minutes it takes to finish 
        # how to count? see how many times the length of the thing gets exceeded
        # which happens at the end

        empty = 0
        fresh = 1
        rotten = 2

        x = len(grid[0])
        y = len(grid)

        q = deque()

        for row in range(y):
            for col in range(x):
                if grid[row][col] == rotten:
                    q.append((row, col))
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        minutes = 0
        track = len(q)
        i = 0

        while q:
            if i == track:
                track = len(q)
                minutes += 1
                i = 0

            row, col = q.popleft()

            for dr, dl in directions:
                new_col = col + dr
                new_row = row + dl
                if new_col < 0 or new_col >= x:
                    continue
                if new_row < 0 or new_row >= y:
                    continue
                if grid[new_row][new_col] != fresh:
                    continue
                grid[new_row][new_col] = 2
                q.append((new_row, new_col))
            i += 1

        print(grid)
        for row in range(y):
            for col in range(x):
                if grid[row][col] == fresh:
                    return -1

        return minutes

        