#2025-10-16 time: 16:10
class Solution(object):
    def pivotIndex(self, nums):
        prefix = 0
        suffix = sum(nums)

        for i, num in enumerate(nums):
            suffix -= num
            if prefix == suffix:
                return i
            prefix+= num

        return -1