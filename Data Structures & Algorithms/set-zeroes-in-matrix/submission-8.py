class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        
        ROWS, COLS = len(matrix), len(matrix[0])
        rowzero = False

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    if i == 0:
                        rowzero = True
                    elif j == 0:
                        matrix[0][0] = 0
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
        
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(ROWS):
                matrix[j][0] = 0
        
        if rowzero == True:
            for i in range(COLS):
                matrix[0][i] = 0

    
            


        
        


        
        