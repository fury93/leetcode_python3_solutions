class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        values = {val for seq in seqs for val in seq}
        graphs = {val:[] for val in values}
        indegrees = {val:0 for val in values}
        for seq in seqs:
            for i in range(len(seq)-1):
                s, t = seq[i], seq[i+1] # source, target
                graphs[s].append(t)
                indegrees[t] += 1
        stack = []
        for val, degree in indegrees.items():
            if degree == 0:
                stack.append(val)
        res = []
        while stack:
            if len(stack) > 1: return False
            s = stack.pop() # source
            res.append(s)
            for t in graphs[s]: # target
                indegrees[t] -= 1
                if indegrees[t] == 0:
                    stack.append(t)
        return len(res) == len(values) and res == org