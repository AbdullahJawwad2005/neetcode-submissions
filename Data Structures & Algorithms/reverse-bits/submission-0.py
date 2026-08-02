class Solution:
    def reverseBits(self, n: int) -> int:
        
        # go over n and 32 and if not divisible by 2 then raise to power

        total = 0
        for i in range (31, -1, -1):
            print(n)
            print(i)
            if n % 2 == 1:
                total += 2**i
            print(total)
            n = n//2
        return total