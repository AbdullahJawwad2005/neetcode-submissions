class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end  = len(matrix) - 1 
        last = len(matrix[0]) - 1
        mid = (start + end)//2

        while(start<=end):
            mid = (end+start)//2
            if (matrix[mid][0]<=target and matrix[mid][last]>=target):
                break
            elif (matrix[mid][0] > target):
                end = mid - 1
            elif (matrix[mid][last] < target):
                start = mid + 1
         

        note = mid
        start = 0
        end = len(matrix[0]) - 1

        while(start<=end):
            mid = (end+start)//2

            if (matrix[note][mid] == target):
                return True
            elif (matrix[note][mid] > target):
                end = mid - 1
            elif (matrix[note][mid] < target):
                start = mid + 1

        print(note)
        print(mid)
        return False

        