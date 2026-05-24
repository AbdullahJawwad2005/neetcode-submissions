class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # a board is a list of lists so we iterate over it using
        # board[row][column]
        # we need to do three things (1) check if each rows
        # have no duplicates there (2) see if each column has no duplicates
        # (3) see if each box has no duplicates. 

        # one thing you could do is make a new array of 9 and iterate o
        # ver each row and column and put it into a set if not already and if it is 
        # then its false

        # then you simply do the same for each box in each row
        for i in range(0, 9): # iterate over each row
            encountered = set() # store for each row
            for j in range(0, 9): # iterate over each column
                if board[i][j] == ".":
                    continue
                if board[i][j] in encountered:
                    print("*")
                    return False
                else:
                    encountered.add(board[i][j])

        for i in range(0, 9): # iterate over each row
            encountered = set() # store for each row
            for j in range(0, 9): # iterate over each column
                if board[j][i] == ".":
                    continue
                if board[j][i] in encountered:
                    print("**")
                    return False
                else:
                    encountered.add(board[j][i])

        # okay assuming both of those are correct
        # then the next thing we do is check each box which can 
        # only be done by making a general set and 3 boxes at once
        for i in range(0, 3):
            for j in range(0, 3):
                encountered = set()
                for y in range(0, 3):
                    for z in range(0, 3):
                        if board[y+i*3][z+j*3] == ".":
                            continue
                        if board[y+i*3][z+j*3] in encountered:
                            print("***")
                            return False
                        else:
                            encountered.add(board[y+i*3][z+j*3])
        return True
        