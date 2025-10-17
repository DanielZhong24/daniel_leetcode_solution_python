#2025-10-17 time: 9:20
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left =0
        right = len(s)-1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if  s[right].lower()!=s[left].lower():
                return False
            left+=1
            right-=1
        return True
        