class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # sort and choose last two
        # go through the array and get the largest and second largest
        #  so what we have to find is the equivalent of the visual which shows
        # a bunch of water between two long bars. its basically length of shortest bar*length between
        # then iterate and check one by one for each 
        i = 0
        j = len(heights) - 1
        best = float('-inf')

        while(i<j):
            container = (j-i)*min(heights[i], heights[j])
            best = max(best, container)
            print(best)

            if(heights[i] > heights[j]):
                j = j - 1
            else:
                i = i + 1
        
        return best

        