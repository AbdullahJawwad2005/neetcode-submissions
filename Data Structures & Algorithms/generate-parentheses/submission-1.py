class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

    
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
            
            
        