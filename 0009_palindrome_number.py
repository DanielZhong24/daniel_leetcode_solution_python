#2025-6-2 time: 3:00
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        i = str(x)
        k = ""
        for j in range(len(i)-1,-1,-1):
            k+= i[j]

        return k == i



