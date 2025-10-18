#2025-6-5 time: 1:09
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """


        s = s.strip().split()

        return len(s[-1])