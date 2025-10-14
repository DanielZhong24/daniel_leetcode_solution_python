#2025-10-14 time: 13:21
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        # choose a DIVISOR
        # divide all array with it and sum <= threshold


        i,j = 1,max(nums)

        maxDivisor = max(nums)

        while i <=j:
            mid = (i+j)//2

            currSum = 0
            for num in nums:
                currSum+= (num+mid-1)//mid
            
            if currSum <= threshold:
                maxDivisor = min(maxDivisor,mid)
                j = mid-1
            else:
                i = mid+1
        return maxDivisor
            