class Solution:
    def countSubstrings(self, s: str) -> int:
        # oh okay so this is similar to the previous problem we did in finding the longest palindrome substring#
        # each individual letter is a substring. then two similar ones are as well
        # I think you iterate over each letter and add one for the palindrome counter, then you check if the two elements
        # on either side are the same and if they are add one or break it
        # if they arent then fuck it
        # now check if its the same as the next element and if it is then do the thing
        # but wait what about duplicates here? doesnt matter, just be careful of edges

        # main for loop
        pal_counter = 0
        for i in range(len(s)):
            pal_counter += 1
            left = i - 1
            right = i + 1
            while right < len(s) and left >= 0 and s[right] == s[left]:
                right += 1
                left -= 1
                pal_counter += 1

            right = i + 1
            left = i

            while right < len(s) and left >= 0 and s[right] == s[left]:
                right += 1
                left -= 1
                pal_counter += 1
        return pal_counter



        