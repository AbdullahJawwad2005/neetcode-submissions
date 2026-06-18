class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
    
        Stack = []
        for i in range(len(s)):
            if s[i] == '{' or s[i] == '('  or s[i] == '[':
                Stack.append(s[i])
            else:
                if not Stack:
                    return False
                if Stack[-1] == '{' and s[i] != '}':
                    return False
                elif Stack[-1] == '[' and s[i] != ']':
                    return False
                elif Stack[-1] == '(' and s[i] != ')':
                    return False
                Stack.pop()
        if not Stack:
            return True
        return False

        