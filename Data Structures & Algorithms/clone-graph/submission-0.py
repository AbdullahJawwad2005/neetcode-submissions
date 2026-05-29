"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # okay I get it now, here we use a hashmap to store neighbours
        # what we need is to iterate over the whole graph in BFS
        # if hasnt been discovered then make and BFS continues
        # if has already been made then link up and end BFS cloning
        # so we need a dict with the original : new addresses 

        if not node:
            return

        visited = {}

        def search(real):
            if real in visited:
                return visited[real]
            
            new = Node(real.val)
            visited[real] = new

            for i in real.neighbors:
                new.neighbors.append(search(i))
            
            return new

        return search(node)



        