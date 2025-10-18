#2025-3-14 time: 16:09
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        d = {
            1:"I",
            4:"IV",
            5:"V",
            9:"IX",
            10:"X",
            40:"XL",
            50:"L",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M"
        }

        result = ""

        for value in sorted(d.keys(),reverse=True):
            while num >= value:
                result+=d[value]
                num -= value
        return result
    
