class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # okay the same dfs approach but now you just append to an array how about that

        # now recreate what you did before. first make an adjacency list
        # then iterate through each node and as you go then add it to the a result list
        # how do you iterate? simple, you check the adjacency list and go through it
        # 
        # 

        # so second is the first one
        # should also have a counter to see if its even valid

        adjacency_list = {i : [] for i in range(numCourses)}
        arr = [0]*numCourses
        visited = set()
        cycle = set()
        results = []

        for i in range(len(prerequisites)):
            crs, pre = prerequisites[i]
            adjacency_list[pre].append(crs)

        counter = 0

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)

            for nxt in adjacency_list[crs]:
                if not dfs(nxt):
                    return False
            
            cycle.remove(crs)
            visited.add(crs)
            results.append(crs)
            return True
                
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        print(visited)
        print(results)
        print(adjacency_list)
        print(counter)
        
        return results[::-1]
        

        


    
        