#2025-3-16 time: 30:17
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        




        def twoSum(nums,target):
            res = []

            left,right = 0, len(nums)-1

            while left < right:
                sum = nums[left]+nums[right]

                if sum < target or(left >0 and nums[left] == nums[left-1]):
                    left +=1
                elif sum > target or(right < len(nums)-1 and nums[right] == nums[right+1]):
                    right -=1
                else:
                    res.append([nums[left],nums[right]])
                    left += 1
                    right -=1 

            return res
        
        def kSum(nums,target,k):
            res = []

            if not nums:
                return res

            average_value = target//k

            if average_value < nums[0] or nums[-1] < average_value:
                return res


            if k == 2:
                return twoSum(nums,target)

            for i in range(len(nums)):
                if i == 0  or nums[i-1] !=nums[i]:
                    for subset in kSum(nums[i+1:],target-nums[i],k-1):
                        res.append([nums[i]]+subset)

            return res
        

        nums.sort()
        return kSum(nums,target,4)



    