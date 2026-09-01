class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n   # index of nearest shorter bar to the left
        right = [n] * n    # index of nearest shorter bar to the right

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        res = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            res = max(res, heights[i] * width)
        return res

        




        

            # put width x length in res array