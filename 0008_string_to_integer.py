#2025-3-12 time: 29:36
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0

        result = ""
        negative = False

        i = 0

        if s[i] in ("+","-"):
            if s[i]=="-":
                negative = True
            i+= 1

        while i<len(s) and s[i].isdigit():
            result+=s[i]
            i+=1

        if not result:
            return 0
        
        num = int(result)
        if negative:
            num = -num
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN

        return num
