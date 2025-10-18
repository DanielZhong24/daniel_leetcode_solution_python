#2025-3-11 time: 5:06
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums1.extend(nums2)

        nums1.sort()

        median = len(nums1)//2

        if len(nums1)%2 == 1:
            return nums1[median]
        else:
            return (nums1[median]+nums1[median-1])/2.0