#2025-10-15 time: 6:33
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []

        nums.sort()

        for k in range(len(nums)):

            if k > 0 and nums[k]==nums[k-1]:
                continue
            i = k+1
            j = len(nums)-1

            while i < j:
                s = nums[k]+nums[i]+nums[j]

                if s == 0:
                    result.append([nums[k],nums[i],nums[j]])

                    i+=1
                    j-=1

                    while i < j and nums[i]==nums[i-1]:
                        i+=1

                    while i < j and nums[j]==nums[j+1]:
                        j-=1
                         
                elif s > 0:
                    j-=1
                else:
                    i+=1
        return result