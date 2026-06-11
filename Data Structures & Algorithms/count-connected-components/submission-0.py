class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # make visited set
        visited = set()


        # make an adjacency list
        adjacency_list = {i:[] for i in range(n)}
        for i in range(len(edges)):
            n1, n2 = edges[i]
            adjacency_list[n1].append(n2)
            adjacency_list[n2].append(n1)



        # make dfs algorithm
        def dfs(prev, edge):
            
            if edge in visited:
                return

            visited.add(edge)

            # iterate through all connected nodes except the one it came from which is previously from
            new = adjacency_list[edge]
            for node in new:
                if node is not prev:
                    dfs(edge, node)
            
        counter = 0
        # iterate through the nodes and dfs then marking if theyre visited or not
        for i in range(n):
            if i in visited:
                continue
            dfs(None, i)
            counter += 1
            print(visited)
            print(counter)

        return counter
    
        # if not visited then dfs and increase by one
        # return the counter by the end
        