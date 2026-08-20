class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                tokens[i] = int(stack.pop()) + int(stack.pop())
                stack.append(tokens[i])
            elif tokens[i] == "*":
                tokens[i] = int(stack.pop())*int(stack.pop())
                stack.append(tokens[i])
            elif tokens[i] == "-":
                tokens[i] = int(stack.pop()) - int(stack.pop())
                stack.append(-tokens[i])
            elif tokens[i] == "/":
                one = int(stack.pop())
                two = int(stack.pop())
                tokens[i] = two/one
                stack.append(tokens[i])
            else:
                stack.append(tokens[i])
        
        print(stack)
        return int(stack[0])
        