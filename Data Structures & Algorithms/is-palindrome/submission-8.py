class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""
        for i in range(len(s)):
            if s[i].isalnum():
                text += s[i].lower()
        return text[::] == text[::-1]
        