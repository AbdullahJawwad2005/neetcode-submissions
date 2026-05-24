class Solution:
    def isValid(self, s: str) -> bool:
        # okay so you iterate through the string then add it
        # first you check out of the six cases
        # if its opening, then you add
        # if its closing then you check and remove or return false
        # if by the end the list is empty you're good

        if not s:
            return False
        counter = []
        
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                counter.append(s[i])
            elif s[i] == ']':
                if len(counter)!=0 and counter[len(counter) - 1] == '[':
                    counter.pop()
                else:
                    return False
            elif s[i] == '}':
                if len(counter)!=0 and counter[len(counter) - 1] == '{':
                    counter.pop()
                else:
                    return False
            elif s[i] == ')':
                if len(counter)!=0 and counter[len(counter) - 1] == '(':
                    counter.pop()
                else:
                    return False
        if len(counter) == 0:
            return True
        return False
        