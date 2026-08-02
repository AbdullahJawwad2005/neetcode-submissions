class Solution:
    def countBits(self, n: int) -> List[int]:

        # okay optimal way to do it is to use dynamic programming


        if n == 0:
            return [0]

        # first initialize the memory buffer
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        


        # iterate over the array and do 1 + dp[i - offset]
        # what this does is find the number of zeros since the last recurring pattern and 
        # add one to it for the next zero
        # how to calculate the offset? if the number % 2 is the last offset then bingo

        # iterate using for loop
        offset = 1
        for i in range(2, n+1):
        # check offset and if thats offset == num % 2 then make that the offset
            if offset == i / 2:
                offset = i
            
            dp[i] = 1 + dp[i - offset]
        
        return dp
        

        # set the current dp as the same as 1 + dp[i - offset], return dp array



        #
        