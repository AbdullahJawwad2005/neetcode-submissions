class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # compare every single letter of the first one to the rest one by one

        first = strs[0]

        prefix = ""
        for letter in first:
            prefix += letter
            for string in strs[1:]:
                if len(string) < len(prefix) or prefix != string[:len(prefix)]:
                    return prefix[:-1]
        return prefix


        