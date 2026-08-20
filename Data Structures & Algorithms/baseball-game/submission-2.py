class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = operations
        l = len(ops)
        i = 0
        while i < l:
            if ops[i] == "+":
                ops[i] = str(int(ops[i-1]) + int(ops[i-2]))
            elif ops[i] == "C":
                ops.pop(i-1)
                ops.pop(i-1)
                i -= 2
            elif ops[i] == "D":
                ops[i] = str(2*int(ops[i-1]))
            i += 1
            l = len(ops)

        print(ops)
        total = 0
        for op in ops:
            total += int(op)
        return total
        
    
                
        