class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in range(len(s)):
            if s[i].isalnum():
                if s[i].isupper():
                    new_s += s[i].lower()
                else:
                    new_s += s[i]
        
  
        return new_s == new_s[::-1] 



        