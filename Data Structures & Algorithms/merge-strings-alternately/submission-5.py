class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        n1 = len(word1)
        n2 = len(word2)
        switch = False
        if n1 < n2:
            n1, n2 = n2, n1
            switch = True

        res = ""
        for i in range(n2):
            res += word1[i]
            res += word2[i]

        if not switch:
            res += word1[n2:]
        else:
            res += word2[n2:]

        return res

        