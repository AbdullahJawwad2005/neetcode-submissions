from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        # here we use topological sort
        # could we make an adjacency list hashmap here? thats probably a better idea
    
        # check if has neighbour, and if doesnt then intialize it or just add one


        preMap = {i : [] for i in range(numCourses)}
        for crs, prq in prerequisites:
            preMap[crs].append(prq)

        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            
            visited.add(crs)

            for prq in preMap[crs]:
                if not dfs(prq):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        
            for crs in preMap:
                if not preMap[crs]:
                    if not dfs(crs):
                        return False

            return True
            
        for crs in preMap:
            if not dfs(crs):
                return False
        return True




        values = [0]*(numCourses)
        for i in range(len(prerequisites)):
            num = prerequisites[i][1]
            values[num] += 1
        
        adjacency_list = {}
        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in adjacency_list:
                num = prerequisites[i][0]
                adjacency_list[num] = [prerequisites[i][1]]
            else:
                adjacency_list[num] = [adjacency_list[num]] + [prerequisites[i][1]]
        
        queue = deque()
        for i in range(len(values)):
            if values[i] == 0:
                queue.append(values[i])
        counter = 1

        while queue:
            counter += 1

            temp = queue.popleft()
            for i in range(len(adjacency_list[temp])):
                temp2 = adjacency_list[temp][i] 
                values[temp2] -= 1
                if values[temp2] == 0:
                    queue.append(values[temp2])

        if counter == numCourses:
            return True
        return False
                
        
            

                
















        tracking = {}
        adjacency_list = {}
        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in tracking:
                tracking[prerequisites[i][0]] = 0
            if prerequisites[i][1] not in tracking:
                tracking[prerequisites[i][1]] = 1
                adjacency_list[prerequisites[i][1]] = [prerequisites[i][0]]
            else:
                tracking[prerequisites[i][1]] += 1
                if prerequisites[i][1] not in adjacency_list:
                    adjacency_list[prerequisites[i][1]] = [prerequisites[i][0]]
                else:
                    adjacency_list[prerequisites[i][1]] = adjacency_list[prerequisites[i][1]] + [prerequisites[i][0]]
        
        # make the queue that takes all the zero values from dict, it might go to multiple nodes so multiple things need to be stored
        # set up while loop that decreases the indegree in the dict for the [i][1]

        # before while loop and in it, go over all
        queue = deque()
        for letter in tracking:
            if tracking[letter] == 0:
                queue.append(letter)
        counter = 1

        while queue:
            counter += 1
            unit = queue.popleft()
            if unit not in adjacency_list:
                continue
            for i in range(len(adjacency_list)):
                tracking[adjacency_list[unit][i]] -= 1

            for letter in tracking:
                if tracking[letter] == 0:
                    queue.add(letter)
    
        if numCourses != counter:
            return False
        return True
        

        