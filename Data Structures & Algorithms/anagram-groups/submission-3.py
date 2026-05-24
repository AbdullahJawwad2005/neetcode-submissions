class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorting = {}
        for i in range(len(strs)):
            new = "".join(sorted(strs[i]))
            if new in sorting:
                sorting[new].append(strs[i])
            else:
                sorting[new] = [strs[i]]
        
        return list(sorting.values())

            
        