class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        counter = 0
        y = len(grid)
        x = len(grid[0])
        visited = set()


        # make a counter
        # hashset that marks things as true

        # backtrack has to just iterate through and once it finds an island, add to the counter and mark everything as visited

        def backTrack(row, col):

            # checks if valid and is 1
            if row >= 0 and row < y and col >= 0 and col < x and (row, col) not in visited and grid[row][col] == '1':
                visited.add((row, col))
            else:
                return
            # if not then return
            print(row, col)

            # if valid then mark as visited

            # then iterates to 4 other options
            backTrack(row-1, col)
            backTrack(row+1, col)
            backTrack(row, col-1)
            backTrack(row, col+1)

        # for loop that goes over all one by one
        for row in range(0, y):
            for col in range(0, x):
                if grid[row][col] == "1" and (row, col) not in visited:
                    counter += 1
                    backTrack(row, col)
        
        return counter

        
        