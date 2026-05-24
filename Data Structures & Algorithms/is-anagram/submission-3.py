class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        chars = [0]*26
        for i in range(len(t)):
            chars[ord(t[i].lower()) - ord("a")] = chars[ord(t[i].lower()) - ord("a")] + 1
            chars[ord(s[i].lower()) - ord("a")] = chars[ord(s[i].lower()) - ord("a")] -1

        for i in range(26):
            if chars[i] != 0:
                return False
        
        return True
        