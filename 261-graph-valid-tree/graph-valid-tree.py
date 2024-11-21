class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        # initialize a parent dict where each vertex belongs to itself
        parent = {i: i for i in range(n)}
        
        # find operation
        def find(v):
            if parent[v] != v:
                # use path compression to gain some time 
                parent[v] = find(parent[v])
            return parent[v]

        for edge in edges:
            # for each edge, check if two vertices belongs to one set
            # if yes then a cycle is found
            set1 = find(edge[0])
            set2 = find(edge[1])
            if set1 == set2:
                return False
                
            # union
            parent[set1] = set2

        return True