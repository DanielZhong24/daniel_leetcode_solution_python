#2025-6-5 time: 10:44
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        
        x = haystack
        for i in range(len(haystack)):
            if x.startswith(needle):
                return i 
            else:
                x = x[1:]

        return -1
    

s = Solution()

print(s.strStr("hello","ll"))

