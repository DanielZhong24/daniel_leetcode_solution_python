#2025-6-11 time: 5:10
class Solution(object):
    def getRow(self, r):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        ans = [1]*(r+1)

        up = r
        down = 1

        for i in range(1,r):
            ans[i] = ans[i-1]*up/down
            up -=1
            down+=1

        return ans
        
