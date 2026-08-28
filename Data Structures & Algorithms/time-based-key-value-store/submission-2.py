from collections import defaultdict

class TimeMap:

    def __init__(self):
        # dictionary for key search, then a list in that for timestamp value
        self.lookup = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # make key in dictionary if not made already (handled by defaultdict)
        # add timestamp and value in a tuple of (value, timestamp)
        self.lookup[key].append((value, timestamp))

        
        

    def get(self, key: str, timestamp: int) -> str:
        # get from dict: self.lookup[key] -> list (search here)
        # edge case: if no values return "" -> if timestamp less that first element of the list

        # binary search -> check middle value, initialize left and right, conditions of finding middle as prev_timestamp if less than equal to timestamp and right is out of bounds or more than timestamp
        # left = middle + 1 if the middle and element on its right are both less than or equal to timestamp
        # right = middle if the middle element is more than timestamp

        key_list = self.lookup[key]
        if key_list and key_list[0][1] > timestamp:
            return ""
        left = 0
        n = len(key_list)
        right = n - 1
        middle = (left+right)//2
        res = ""

        while left <= right:
            middle = (left+right)//2
            if key_list[middle][1] <= timestamp:
                res = key_list[middle][0]
                left = middle + 1
            else:
                right = middle - 1
        
        return res




        # [1, 3, 4, 8, 9]

        
