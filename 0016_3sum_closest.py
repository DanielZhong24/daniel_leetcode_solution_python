#2025-3-16 time: 17:10
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()

        n = len(nums)
        result = float('inf')
        for i in range(n-2):
            if i >0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = n-1

            while left < right:
                sum= nums[i] + nums[left]+nums[right]

                if sum == target:
                    return target
                
                if abs(sum-target) < abs(result-target):
                    result = sum

                
                if sum < target:
                    left += 1
                else:
                    right -=1

        return result