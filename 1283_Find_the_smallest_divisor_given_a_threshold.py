#2025-10-15 time: 12:04
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """

        minDivisor = max(nums)
        i,j = 1,max(nums)

        while i <= j:
            mid = (i+j)//2

            currSum = 0
            for num in nums:
                currSum += (num+mid-1)//mid
            if currSum <= threshold:
                minDivisor = min(minDivisor,mid)
                j=mid-1
            else:
                i=mid+1
        
        return minDivisor

        