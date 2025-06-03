#2025-6-3 time: 5:00
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""
        
        prefix  = strs[0]


        for str in strs[1:]:
            while not str.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""
                
        return prefix






        