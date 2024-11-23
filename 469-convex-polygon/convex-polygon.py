class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        def direction(a,b,c):
            return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
        d = None
        for i in range(1,len(points)):
            a = direction(points[i-2],points[i-1],points[i])
            if a == 0: continue
            if d == None: d = a
            else:
                if a*d < 0: return False
        if direction(points[-2],points[-1],points[0]) * d < 0:return False
        return True