class segment_tree(object):


    # minimum value, change if needed
    def merge(self,num,accu):
        if self.flag: return min(accu,num)
        else:  return max(accu,num)


    def __init__(self,n,initial,flag):

        self.n = n
        self.flag = flag
        if self.flag:  self.inf = float('inf')
        else:  self.inf = -float('inf')
        self.arr = [self.inf]*(2*n)
        for i in range(2*n-1,0,-1):
            if i>=n:  self.arr[i] = initial[i-n]
            else:     self.arr[i] = self.merge(self.arr[2*i],self.arr[2*i+1])




    def update(self,index,target):
        index += self.n
        self.arr[index] = target
        while index > 0:
            if index & 1:
                nexttarget = self.merge( self.arr[index], self.arr[index-1])
            else:
                nexttarget = self.merge( self.arr[index], self.arr[index+1])
            self.arr[index>>1] = nexttarget 
            index = index >> 1


    def addnum(self,index,diff):
        self.update(index, self.arr[index+self.n] + diff)


    def query(self,left,right):
        i,j = self.n+left,  self.n+right+1
        output = self.inf  # initial output should be changed if you want to change the merge function

        while i<j:
            if i&1:
                output = self.merge(self.arr[i],output)
                i += 1
            if j&1:
                j -= 1
                output = self.merge(self.arr[j],output)
            i = i >> 1
            j = j >> 1
        return output





class Solution(object):
    def maxProfit(self, prices, profits):
        """
        :type prices: List[int]
        :type profits: List[int]
        :rtype: int
        """
        n = len(prices)
        nums = sorted(prices)

        # map the prices to a mapping table to save memory
        mapping = {}
        for num in nums:
            if num in mapping:  continue
            mapping[num] = len(mapping)
        m = len(mapping)

        
        # maxleft means maximum left point profit, and maxright is maximum right point profit. 

        maxleft = [-1]*n
        maxright = [-1]*n

        segleft = segment_tree(m,[-1]*m,False)
        segright = segment_tree(m,[-1]*m,False)

        # valueleft and valueright is the current max profit on this point,  if mapping[prices[i]] is no smaller than current profit,  we don't need to update
        valueleft = [-1]*m
        valueright = [-1]*m

        # update the left segment_tree, each operation is O(n lg n)
        for i in range(n):
            index = mapping[prices[i]]
            maxleft[i] = segleft.query(0,index-1)
            if(profits[i] > valueleft[index]):
                valueleft[index] = profits[i]
                segleft.update(index,profits[i])

        # update the right segment_tree,  each operation is O(n lg n)
        for i in range(n-1,-1,-1):
            index = mapping[prices[i]]
            maxright[i] = segright.query(index+1,m-1)
            if(profits[i] > valueright[index]):
                valueright[index] = profits[i]
                segright.update(index,profits[i])

        # check the answer using maxleft and maxrigiht
        ans = -1
        for i in range(n):
            if maxleft[i]<0 or maxright[i]<0: continue
            ans = max(ans, profits[i]+maxleft[i]+maxright[i])
        return ans