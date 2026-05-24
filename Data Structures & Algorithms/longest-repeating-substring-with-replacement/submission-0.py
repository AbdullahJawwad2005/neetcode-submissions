class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # okay this is a sliding window problem
        # ends when hits the end
        # start increments when theres too many nonlargest characters in the hashset
        # so you increment and keep removing until the condition is finally met
        # which is length of substring - frequency of most frequent <= k
        # the end increments after each loop
        # the best stores the longes which can be done like this

        # set up best and start and end
        # implement the while for sliding window
        # condition for start to increment plus a while loop inside to keep going until its sure
        # update best
        # end = end + 1

        start = 0
        end = 1
        best = 1
        encountered = {}
        encountered[s[start]] = 1

        while(end<len(s)):
            if s[end] in encountered:
                encountered[s[end]] += 1
            else: 
                encountered[s[end]] = 1
            print(s[start:end])
            
            while len(s[start:end]) - max(encountered.values()) >= k:
                encountered[s[start]] -= 1
                start = start + 1
            
            
            best = max(best, len(s[start:end+1]))
            end = end + 1
        
        return best



        
        





        