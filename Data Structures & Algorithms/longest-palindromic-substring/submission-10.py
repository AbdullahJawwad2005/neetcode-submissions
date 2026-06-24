class Solution:
    def longestPalindrome(self, s: str) -> str:
        # okay the brute force solution is recursively checking across every letter as the center (but two letters might be the center)
        # we want an O(n) solution, how do we find the recursive case? how is a longest palindrome found? test all the substrings
        # thats way too long of a solution. test all the letters in general I think, using one as a center or two as a center
        # lets check if thats close to the correct solution, okay so the idea for my solution was correct
        # lets give this a shot now
        if not s:
            return s

        maxlen = 0
        start = 0

        for i in range(len(s)):
            center = s[i]
            # find the center then expand outwards from it and store maxlength and where it starts from
            # check if the left and right sides are inside then check if theyre the same, if they are then update maxlen then increment
            left = i - 1
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                # the one in left is equal to right then you keep incrementing and replace the max and start for stored
                if s[left] == s[right]:
                    if maxlen < (right-left + 1):
                        maxlen = right - left + 1
                        start = left
                left = left - 1
                right = right + 1

            # check if its not the last and then check if its equal to the next
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and left != len(s) - 1 and s[left] == s[right]:
                if s[left] == s[right]:
                    if maxlen < (right-left + 1):
                        maxlen = right - left + 1
                        start = left
                left = left - 1
                right = right + 1
        
        if maxlen == 0:
            maxlen = 1
        return s[start:start+maxlen]
        