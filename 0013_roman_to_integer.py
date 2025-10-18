#2025-6-2 time: 8:29
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {
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
            current = d[s[i]]

            next  = d[s[i+1]]

            if current < next:
                num -= current
            else:
                num+= current

        return num+d[s[-1]]