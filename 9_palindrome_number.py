#2025-3-12 time: 3:10
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        org = x
        temp = 0
        while x > 0:
            temp = temp*10 + x%10
            x//=10
        return temp == org


