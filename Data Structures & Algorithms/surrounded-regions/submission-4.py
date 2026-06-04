class Solution:
    def solve(self, board: List[List[str]]) -> None:

        y = len(board)
        x = len(board[0])

        edge_circles = set()
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for col in range(x):
            if board[0][col] == "O":
                edge_circles.add((0, col))
            if board[y-1][col] == "O":
                edge_circles.add((y-1, col))

        for row in range(y):
            if board[row][0] == "O":
                edge_circles.add((row, 0))
            if board[row][x-1] == "O":
                edge_circles.add((row, x-1))

        
        def DFS(edge):
            row, col = edge

            if row >= y or row < 0 or col >= x or col < 0 or board[row][col] == "X" or (row, col) in visited:
                return

            if board[row][col] == "O":
                visited.add((row, col))
            
            DFS((row + 1, col))
            DFS((row, col + 1))
            DFS((row - 1, col))
            DFS((row, col - 1))

        
        for edge in edge_circles:
            DFS(edge)
        
        print(visited)

        for row in range(y):
            for col in range(x):
                if (row, col) not in visited:
                    board[row][col] = "X"

        