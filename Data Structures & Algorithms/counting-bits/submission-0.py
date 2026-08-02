class Solution:
    def countBits(self, n: int) -> List[int]:

        # set up counter
    

        output = []

        arr = [i for i in range(0, n+1)]
        # iterate using for loop
        for elem in arr:
            counter = 0
            while elem != 0:
                if elem % 2 == 1:
                    counter += 1
                elem = elem // 2
            output.append(counter)
        return output

        