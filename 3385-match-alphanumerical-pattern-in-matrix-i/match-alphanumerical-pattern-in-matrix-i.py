class Solution:
    def findPattern(self, board, pattern):
        def check_function(s,t):
            dict_s, dict_t = {}, {}

            for i,j in zip(s,t):
                if i.isdigit() and j.isdigit():
                    if i != j: return False 
                else:
                    if i not in dict_s:
                        dict_s[i] = j 
                    else:
                        if dict_s[i] != j: 
                            return False 

            for i,j in zip(t,s):
                if i.isdigit() and j.isdigit():
                    if i != j: return False 
                else:
                    if i not in dict_t:
                        dict_t[i] = j 
                    else:
                        if dict_t[i] != j:
                            return False 

            return True 


        m, n, dict1, ans = len(pattern), len(pattern[0]), defaultdict(int), "".join(pattern)

        for i in range(len(board)-m+1):
            for j in range(len(board[0])-n+1):
                result = ""
                for k in range(i,i+m):
                    for l in range(j,j+n):
                        result += str(board[k][l])
                dict1[(i,j)] = check_function(result,ans)

        bill_gates = []

        for i in dict1:
            if dict1[i] == True:
                bill_gates.append([i[0],i[1]])

        bill_gates.sort(key = lambda x:(x[0],x[1]))

        return bill_gates[0] if bill_gates else [-1,-1]