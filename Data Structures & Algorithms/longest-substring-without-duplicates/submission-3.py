class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashMap = {}
        maxLength = 0
        left = 0

        for right in range(len(s)):
            if s[right] in hashMap:
                left = max(hashMap[s[right]] + 1, left)
            hashMap[s[right]] = right
            maxLength = max(maxLength, right - left + 1) 
        
        return maxLength