#2025-6-6 time: 13:57
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n<=2:return n

        p = [0]*(n+1)

        p[1]=1
        p[2]=2

        for i in range(3,n+1):
            p[i] = p[i-1]+p[i-2]

        return p[n]        
    