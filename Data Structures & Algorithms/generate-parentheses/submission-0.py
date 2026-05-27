class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # okay here we have to use backtracking in order to create a proper order of parenthesis
        # to work what are the conditions? Paramaters? with and without cases
        # one thing we can do is use a counter for open parenthesis and only do closed if there are less than open, and mandatory when reach limit

        res = []
        def backTrack(string, n , opened, closed):
            # base case
            if n == opened and n == closed:
                res.append(string[:])
                return
            print(string)
            # with
            if n > opened:
                backTrack(string+"(", n, opened + 1, closed)
            if closed < opened:
                backTrack(string+")", n, opened, closed+1)
            
        backTrack("", n, 0, 0)
        return res
            
            
            # without
        