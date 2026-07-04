class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        # use the bottom and the left rows and col to mark zero and when the rest of it needs to be zero
        # then go over it in two passes

        # for the first box have a single variable that decides whether or not something else is it


        # so for the first pass go over all and everytime you see a zero then mark the top row and left col 
        # of that specific spot
        # for loop (i)
        left = 1
        top = 1
        for i in range(len(matrix)):
            # for loop (j)
            for j in range(len(matrix[0])):
                if (i == 0 or j == 0) and matrix[i][j] == 0:
                    if i == 0:
                        top = 0
                    if j == 0:
                        left = 0
                elif matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

                # if zero mark its top and left parts 0
                # if its the first column then if its on the left mark the variable if its on the top mark the left column


        # for the next one go through them all and and check if either their left row or top col is zero
        # if it is then turn to zero
        print(matrix)
        matrix2 = matrix

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix2[i][0] == 0 or matrix2[0][j] == 0:
                    matrix[i][j] = 0

        if top == 0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if left == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0


        


        
        