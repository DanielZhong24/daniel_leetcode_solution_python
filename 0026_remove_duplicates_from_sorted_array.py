#2025-6-3 time: 9:22
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0


        check = []
        k = 0

        for num in nums:
            if num not in check:
                check.append(num)
                k+=1
        nums[:] = check
        
        return k

        