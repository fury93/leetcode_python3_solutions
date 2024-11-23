class Solutio2(object):
    def findContestMatch(self, n):
        team = map(str, range(1, n+1))

        while n > 1:
            for i in range(n // 2):
                team[i] = "({},{})".format(team[i], team.pop())
            n /= 2

        return team[0]

class Solution(object):
    def findContestMatch(self, n):
        team = []
        ans = []
        def write(r):
            if r == 0:
                i = len(team)
                w = i & -i
                team.append(n//w+1 - team[i-w] if w else 1)
                ans.append(str(team[-1]))
            else:
                ans.append("(")
                write(r-1)
                ans.append(",")
                write(r-1)
                ans.append(")")

        write(int(math.log(n, 2)))
        return "".join(ans)