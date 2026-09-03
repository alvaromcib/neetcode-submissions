class Solution:

    def quickSort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: 
            return nums

        p = nums[-1]
        L = [x for x in nums[:-1] if x <= p]
        R = [x for x in nums[:-1] if x > p]

        L = self.quickSort(L)
        R = self.quickSort(R)

        return L + [p] + R

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        triplets = []

        for i in range(len(nums)): 
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = nums[l] + nums[r] + nums[i] 
                
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    triplets.append([nums[i],nums[l], nums[r]])
                    l += 1
                    while (nums[l] == nums[l-1]) and l < r: l+= 1
        
        return triplets
        