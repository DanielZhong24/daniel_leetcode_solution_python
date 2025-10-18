#2025-3-11 time: 18:17
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        longest = ""
        def expand(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1:right]
        
        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i,i+1)

            longest = max(longest,odd,even,key=len)
        return longest
        
        
        
        
        
        
        
        
        #run time too long
    
        # if len(s) == 0:
        #     return ""
        # def isPalindrome(x):
        #     flip = ""
        #     for i in range(len(x)-1,-1,-1):
        #         flip+= x[i]

        #     return flip == x
        
        # curr = s[0]
        # longest = 1

        # for i in range(len(s)-1):
        #     temp = s[i]
        #     for j in range(i+1,len(s)):
        #         if isPalindrome(temp) and len(temp) > longest:
        #             longest = len(temp)
        #             curr = temp
        #         temp+= s[j]
        
        # return curr
    

