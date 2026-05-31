from collections import deque
from typing import List

 


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # given an m x n 2D grid with 3 possible values. -1 = impassible water. 0 is a treasure chest. INF is a land cell of INF
        # fill in each land cell with distance to nearest chest. if unable, then INF
        # modify grid in place
        # so what algorithm? we need a BFS here. something that returns the min length. then puts it on the grid
        # iterates to all land cells
        # be careful for the distance to not be zero and not count water cells

        if not grid:
            return 

        treasure = 0
        water = -1
        land = 2147483647
        y = len(grid)
        x = len(grid[0])
        
        chests = deque()

        for row in range(y):
            for col in range(x):
                if grid[row][col] == treasure:
                    chests.append((row, col))
        
        # okay what we have to do here is keep popping and seeing if anything near it is land, then give it a distance of 1
        # if its not a 1 then just skip it entirely and if its zero then something else
        while chests:
            row, col = chests.popleft()
            # now check what around it is land and give it the value of itself + 1 and append it
            # how do you prevent overlap? simple if its not land then you dont go over it and continue

            directions = [(0, 1), (1, 0), (-1, 0), (0,-1)]
            print(row, col)
            for dr, dl in directions:
                new_col = col + dr
                new_row = row + dl
                if new_col < 0 or new_col >= x:
                    continue
                if new_row < 0 or new_row >= y:
                    continue
                if grid[new_row][new_col] != land:
                    continue
                grid[new_row][new_col] = 1 + grid[row][col]
                chests.append((new_row, new_col))

        

        