class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # okay this works as depth first search on every letter in the array
        # array traversal basically
        # use a hashset to prevent revisiting
        # if string > len(word) then remove the start and keep going
        # 4 cases are 
        visited = set()
        n = len(word)
        y = len(board)
        x = len(board[0]) 

        def backTrack(board, col, row, i):
            # base case

            if i == len(word):
                return True

            if (row < 0 or col < 0 or row >= y or col >= x or (row, col) in visited):
                return False
            if word[i] != board[row][col]:
                return False

            visited.add((row, col))
            
        
            res = (backTrack(board, col, row+1, i+1) or 
                    backTrack(board, col+1, row, i+1) or 
                    backTrack(board, col, row-1, i+1) or
                    backTrack(board, col-1, row, i+1))
            
            visited.remove((row, col))
            
            return res
            

        for row in range(y):
            for col in range(x):
                visited = set()
                if backTrack(board, col, row, 0) == True:
                    return True
        
        return False



        