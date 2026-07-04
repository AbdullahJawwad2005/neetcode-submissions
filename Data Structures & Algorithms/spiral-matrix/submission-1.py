class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # okay we use two while loops here
        rows = len(matrix)
        cols = len(matrix[0])

        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        order = []

        while True:
            
            for i in range(left, right):
                order.append(matrix[top][i])
            
            top += 1

            for i in range(top, bottom):
                order.append(matrix[i][right-1])
            
            right -= 1

            if not (left<right and top<bottom):
                break
            
            print(order)
            for i in range(right-1, left-1, - 1):
                order.append(matrix[bottom-1][i])
            
            bottom -= 1

            for i in range(bottom-1, top-1, -1):
                order.append(matrix[i][left])
            
            left += 1

            if not (left<right and top<bottom):
                break


        return order

        