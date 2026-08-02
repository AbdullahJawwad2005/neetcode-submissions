class Solution:
    def reverseBits(self, n: int) -> int:
        

        total = 0
        for i in range (31, -1, -1):
            if n % 2 == 1:
                total += 2**i
            n = n//2
        return total