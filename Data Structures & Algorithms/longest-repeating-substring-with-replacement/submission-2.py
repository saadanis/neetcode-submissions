class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freqMap = defaultdict(int)
        left = 0
        maxGlobal = 0
        maxLocal = 0

        for right in range(len(s)):
            freqMap[s[right]] += 1
            maxLocal = max(maxLocal, freqMap[s[right]])

            while right - left + 1 - maxLocal > k:
                freqMap[s[left]] -= 1
                left += 1
            
            maxGlobal = max(maxGlobal, right - left + 1)
        
        return maxGlobal
