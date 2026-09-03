class Solution:

    def maxArea(self, heights: List[int]) -> int:
        max_value = -1

        l = 0
        r = len(heights) - 1

        while l < r: 

            area_value = (r-l) * min(heights[r], heights[l])

            max_value = max(max_value, area_value)

            if heights[l] >= heights[r]: 
                r -= 1
            else: 
                l += 1
        
        return max_value
