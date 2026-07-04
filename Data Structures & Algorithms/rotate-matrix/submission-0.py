class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # just flip the columns and rows and its done, so its a simple temp swap function
        # it needs to start from one column and one row ahead each time to not reswap anything


        # for loop (i)
            # for loop within for loop (j)
                    # swap [i][j] with [j][i]

        for i in range(0, len(matrix)):
            for j in range(i, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                print(i, j)

        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                # swap across the middle line of symmetry
                # so swap matrix[i][j] with matrix[i][len - 1 - j]
                matrix[i][j], matrix[i][len(matrix) -1 - j] = matrix[i][len(matrix) -1 - j], matrix[i][j]
 

