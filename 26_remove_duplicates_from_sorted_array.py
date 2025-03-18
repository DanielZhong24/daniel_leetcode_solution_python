#2025-3-18 time: 5:06
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        

        r = 0

        for i in range(1,len(nums)):
            if nums[i] != nums[r]:
                r+=1
                nums[r] = nums[i]

        return r+1