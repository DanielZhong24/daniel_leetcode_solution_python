#2025-3-11 time: 11:21
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        longest = 1

        for i in range(len(s)-1):
            streak = 1
            exist = []
            exist.append(s[i])
            for j in range(i+1,len(s)):
                if s[j] in exist:
                    break
                streak += 1
                exist.append(s[j])

            longest = max(streak,longest)

        return longest
