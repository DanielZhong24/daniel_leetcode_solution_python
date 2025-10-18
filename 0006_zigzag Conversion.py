#2025-3-12 time: 30:20
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or numRows >= len(s):
            return s

        result = ['']*numRows

        index = 0
        step = 1

        for x in s:
            result[index] += x
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step

        return ''.join(result)
