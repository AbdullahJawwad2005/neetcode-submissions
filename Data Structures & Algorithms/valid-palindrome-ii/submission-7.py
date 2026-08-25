class Solution:
    def validPalindrome(self, s: str) -> bool:
        # brute force is try deleting one of every character until you get positive

        # what you can do better is delete the mismatched character, but you dont know that until you test all

        # you can test normally. then delete one where it doesn't work. how would a greedy solution look like for this though? 

        # you can have a switch. that can sustain max one mismatch. if its more than one then nah

        left = 0
        right = len(s) - 1
        switch = True

        while left < right:
            if s[left] != s[right]:
                skipL = s[left+1:right+1]
                skipR = s[left:right]
                print(skipR, skipL)
                return skipR[::]==skipR[::-1] or skipL[::]==skipL[::-1]
            else:     
                left += 1
                right -= 1
        
        return True
        