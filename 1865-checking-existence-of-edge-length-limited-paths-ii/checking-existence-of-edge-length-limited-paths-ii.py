class DistanceLimitedPathsExist(object):

    def __init__(self, n, edgeList):
        def find(node):
            if parent[node]!=node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(x,y):
            parent[find(y)] = find(x)
            return
        
        parent = {i:i for i in range(n)}# parent for each node
        edgeList.sort(key = lambda x:x[2])
        self.connections = []
        self.weights = []
        for index,(i,j,weight) in enumerate(edgeList):# for cur weight, connect i,j
            union(i,j)
            if index!=len(edgeList)-1 and weight == edgeList[index+1][2]:
                continue
            self.weights.append(weight) # save the weight keys
            self.connections.append([find(i) for i in parent])# save the connection for cur weight
            

    def query(self, p, q, limit):
        index = bisect.bisect_left(self.weights,limit)
        if index==0:
            return False
        return self.connections[index-1][p] == self.connections[index-1][q]     


# Your DistanceLimitedPathsExist object will be instantiated and called as such:
# obj = DistanceLimitedPathsExist(n, edgeList)
# param_1 = obj.query(p,q,limit)