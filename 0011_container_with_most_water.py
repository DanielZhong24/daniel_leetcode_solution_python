#2025-10-18 time: 5:00
class Solution:
    def maxArea(self, heights) -> int:
        
        left = 0
        right = len(heights)-1
        area = 0
        while left < right:
            a = (right-left)* min(heights[left],heights[right])
            area = max(a,area)

            if heights[left]< heights[right]:
                left+=1
            else:
                right-=1

        return area