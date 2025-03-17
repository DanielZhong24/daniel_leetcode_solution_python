#2025-3-16 time: 6:17
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        d = {
            "(":")",
            "[":"]",
            "{":"}"
        }

        stack = []
        for x in s:
            if x in d:
                stack.append(x)
            elif len(stack) == 0 or d[stack.pop()] != x:
                return False
            
        return len(stack) == 0
