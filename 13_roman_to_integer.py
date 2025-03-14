#2025-3-14 time: 4:33
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        value = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        num = 0

        for i in range(len(s)-1):
            current  = value[s[i]]
            next = value[s[i+1]]

            if current < next:
                num -= current
            else:
                num += current

        return num + value[s[-1]]