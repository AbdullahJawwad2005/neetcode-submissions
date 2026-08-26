class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # implement a stack
        # if the stack has nothing in it you make the result a 0 and add the element to a stack with its index
        # if it does check if the last element of the stack is lesser compared to it, if it is then pop and check the next and if its more then add to it with the index and add the index - the current index together

        stack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            while stack:
                if stack[-1][1] > temperatures[i]:  # more than case
                    res[i] = stack[-1][0] - i
                    stack.append((i, temperatures[i]))
                    break
                else: # less than or equal to case:
                    stack.pop()
            if not stack: 
                stack.append((i, temperatures[i]))
                res[i] = 0
        
        return res
        