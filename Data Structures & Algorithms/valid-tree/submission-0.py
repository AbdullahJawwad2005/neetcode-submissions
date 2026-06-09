class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # so basically every node is connected and no cycles.
        # also represented using an adjacency list
        # how can we represent this? 
        # using dfs until the cycle happens? like we did before? that would solve the problem for the cycle
        # what it wouldnt solve would be the problem of the disconnected nodes
        # we can solve that by not iterating through the entire code and only from one node, since its undirected

        # make visited and cycle sets
        visited = set()
        cycle = set()
        adjacency_list = {i : [] for i in range(n)}


        # make adjacency list
        for i in range(len(edges)):
            one, two = edges[i] 
            adjacency_list[one].append(two)
            adjacency_list[two].append(one)


        # implement dfs
        def dfs(prev, edg):
            if edg in visited:
                return True

            if edg in cycle:
                return False
            

            cycle.add(edg)

            for node in adjacency_list[edg]:
                if node is prev:
                    continue
                if not dfs(edg, node):
                    return False
            
            cycle.remove(edg)

            visited.add(edg)
                
            return True


        # run dfs and return false if cycle
        if not dfs(None, 0):
            return False

        # check if len of visited is the same as the rest
        if len(visited) != n:
            return False

        # return true then
        return True


        

        