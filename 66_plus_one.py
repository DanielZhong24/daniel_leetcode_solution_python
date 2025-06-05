#2025-6-5 time: 5:41
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        digit = 0

        for i in range(len(digits)):
            digit += digits[i] *(10**(len(digits)-i-1))


        digit +=1
        result = []

        while digit >0:
            x = digit%10
            result.insert(0,x)
            digit = digit//10

        return result
    

s = Solution()

print(s.plusOne([9]))