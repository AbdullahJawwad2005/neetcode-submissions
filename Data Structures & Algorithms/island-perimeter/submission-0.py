class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # dfs from every point and as long as its not in visited and not water then dfs


        # when you dfs, if the next cell is water or out of bounds then do a +1 on the perimeter. if its not then do the same for it.
        # its not +1, its returning and summing all the perimeters for its part.


        # you dont only have to go over the entire thing just until you find the first land block

        visited = set()
        max_row = len(grid)
        max_col = len(grid[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(row, col):   
            print(row, col)
            # if out of bounds
            if row < 0 or row >= max_row or col < 0 or col >= max_col:
                return 1

            # if water
            if grid[row][col] == 0:
                return 1

            # if in visited
            if (row, col) in visited:
                return 0
            # RETURN 0

            visited.add((row, col))


            count = 0

            for direct in directions:
                count += dfs(direct[0] + row, direct[1] + col)

            return count
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)

            




            #
            #
        