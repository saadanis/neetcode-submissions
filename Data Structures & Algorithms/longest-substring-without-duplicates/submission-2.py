class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        substring = set()
        maxLength = 0

        left = 0

        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
            substring.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength