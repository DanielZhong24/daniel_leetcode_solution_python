#2025-3-12 time: 9:01
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        #first try on two pointer approach
        #start from the widest possible container and move to the inside

        left,right = 0, len(height)-1
        max_area = 0
        while left < right:
            area = min(height[left],height[right]) *(right-left)
            max_area = max(max_area,area)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return max_area