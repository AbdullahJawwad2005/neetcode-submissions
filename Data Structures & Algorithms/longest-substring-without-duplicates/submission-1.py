class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # okay I can see the issue we're having here
        # what we basically have to do is make a sliding window
        # everytime the right one gets to something that is already in the set
        # you drop it and everything that comes before it
        # whats the best data structure to use here? probably a set
        # and use a for loop when detects a duplicate to drop off everything before then


        unique = set()
        best = 0
        l = 0

        for i in range(len(s)):
            if s[i] not in unique:
                unique.add(s[i])
            else:
                while(s[i] in unique):
                    unique.remove(s[l])
                    l = l + 1
                unique.add(s[i])
            print(unique)
            best = max(best, len(unique))
    
        return best







        
        
        