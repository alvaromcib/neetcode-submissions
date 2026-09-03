class Solution:
    def area(self, base: int, height: int) -> int: 
        return base * height

    def maxArea(self, heights: List[int]) -> int:
        max_value = -1

        l = 0
        r = len(heights) - 1

        while l < r: 
            base = r-l
            height = min(heights[r], heights[l])

            area_value = self.area(base, height)

            max_value = max(max_value, area_value)

            if heights[l] >= heights[r]: 
                r -= 1
            else: 
                l += 1
        
        return max_value
