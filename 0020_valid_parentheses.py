#2025-6-3 time: 10:00
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 != 0:
            return False

        d={"(":")","{":"}","[":"]"}



        queue = []

        for bracket in s:
            if bracket in d:
                queue.append(bracket)

            else:
                if not queue or d[queue[-1]] != bracket:
                    return False
                queue.pop()
            
        return len(queue) == 0

s = Solution()

print(s.isValid('(([]))[]['))

        

            




        