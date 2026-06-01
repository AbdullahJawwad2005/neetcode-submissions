class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # represents height above sea level
        # water flows from higher to equal or lower or to ocean if near
        # find all cells where water flows to both pacific and atlantic oceans from there
        # so we need to find a cell which reaches col < 0 and col > x with water
        
        # so start with reverse DFS to find all cells that can flow to pacific and atlantic and see overlap and return those
        atlantic_flow = set()
        pacific_flow = set()

        y = len(heights)
        x = len(heights[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def DFS_a(row, col, prev):

            # add boundary conditions
            if row < 0 or row >= y or col < 0 or col >= x:
                return 

            # see if its greater than previous
            curr = heights[row][col]
            if curr < prev or (row, col) in atlantic_flow:
                return

            # if yes then add it to the set
            atlantic_flow.add((row, col))

            for dr, dl in directions:
                DFS_a(row+dr, col+dl, curr)
            
        def DFS_p(row, col, prev):

            # add boundary conditions
            if row < 0 or row >= y or col < 0 or col >= x:
                return 

            # see if its greater than previous
            curr = heights[row][col]
            if curr < prev or (row, col) in pacific_flow:
                return

            # if yes then add it to the set
            pacific_flow.add((row, col))

            for dr, dl in directions:
                DFS_p(row+dr, col+dl, curr)
            


        # pacific values
        for i in range(y):
            DFS_p(i, 0, 0)
            DFS_a(i, x-1, 0)
        for i in range(x):
            DFS_p(0, i, 0)
            DFS_a(y-1, i, 0)
        
        res = []
        print(atlantic_flow)
        print(pacific_flow)
        for i in range(y):
            for j in range(x):
                if (i, j) in pacific_flow and (i, j) in atlantic_flow:
                    res.append([i, j])

        return res

        
        