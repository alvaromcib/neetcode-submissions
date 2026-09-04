class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        subs = set()
        max_length = 0

        l = 0
        n = len(s)

        for r in range(len(s)):

            while s[r] in subs:
                subs.remove(s[l]) 
                l += 1
            
            subs.add(s[r])
            max_length = max(max_length, r - l + 1)

        
        return max_length
                






        