class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        matches = {}                        # Stores matches formed. key = girl, value = boy.
        
        def dfs(boy: int, visited: set) -> bool:
            """A depth first search function to match a boy at index `boy` with potential girls.
            
            DFS will go through all of the boy's options and choose the one that maximizes global
            optimum.
            """
            
            for girl in range(N):
                
                # Rule 1. Only ask that girl if you haven't asked her before already.
                # Rule 2. If you wish to ask a girl that's taken, she will only go with you
                #         if her current partner finds a new girl.
                
                if grid[boy][girl] and girl not in visited:
                    visited.add(girl)
                    
                    if girl not in matches or dfs(matches[girl], visited): 
                        matches[girl] = boy                        
                        return True
                
            return False
            
        for boy in range(M):
            dfs(boy, set())
            
        return len(matches)