class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # okay pretty simple sliding window problem
        # general thing I can see here is to go over it using sliding window and store occurences in 
        # a dictionary. you keep checking if its right in every instance
        # this should be a fixed window problem, like it keeps on going while being fixed. and at the end
        # its done. s1 is always smaller so will be the one being checked against
        # how do you check one dictionary against it though?
        # okay no dictionary needed we use the array and ord method. thats enough, by intializing an array
        # to only 26 spaces and its already lower case so we don't have to worry about that
        # how do you check it though? by making a loop before that takes everything in another array
        # then you just compare each array at each point

        if len(s1) > len(s2):
            return False
        
        arr1 = [0]*26
        for i in range(len(s1)):
            arr1[ord('a') - ord(s1[i]) + 1] += 1

        
        start = 0
        end = 0
        arr2 = [0]*26


        while(end - start != len(s1)):
                arr2[ord('a') - ord(s2[end]) + 1] += 1
                end = end + 1
                print(arr2)
        if arr2==arr1:
                return True
        while(end!=len(s2)):

            arr2[ord('a') - ord(s2[end]) + 1] += 1

            arr2[ord('a') - ord(s2[start]) + 1] -= 1
            start = start + 1
            end = end + 1
            print(arr2)
            if arr2==arr1:
                return True
        
        return False
        