#2025-10-22 time: 3:39
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False


        d = {")":"(","}":"{","]":"["}
        stack= []

        for p in s:
            if p in d.keys() and len(stack)>0:
                if stack[-1] != d[p]:
                    return False
                else:
                    stack.pop()

            else:
                stack.append(p)

        return len(stack)==0

