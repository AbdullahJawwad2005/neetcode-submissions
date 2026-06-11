class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        class UnionFind:
            def __init__(self, size):
                self.rank = [1]*size
                self.parents = [i for i in range(size)]
            
            def find(self, n1):
                
                while n1 != self.parents[n1]:
                    n1 = self.parents[n1]
                
                return n1

            def union(self, n1, n2):
                root_x = self.find(n1)
                root_y = self.find(n2)

                if root_x == root_y:
                    return 0
                
                if self.rank[root_x] > self.rank[root_y]:
                    self.parents[root_y] = root_x
                elif self.rank[root_x] < self.rank[root_y]:
                    self.parents[root_x] = root_y
                else:
                    self.parents[root_y] = root_x
                    self.rank[root_x] += self.rank[root_y]
                
                return 1
        uf = UnionFind(n)
        res = n
        for n1, n2 in edges:
            res -= uf.union(n1, n2)
        return res
