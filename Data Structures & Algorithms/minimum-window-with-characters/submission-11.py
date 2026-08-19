class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        freqT = defaultdict(int)
        freqSubS = defaultdict(int)
        res = ""

        for c in t:
            freqT[c] += 1

        left = 0
        right = 0

        have = 0

        while left <= right and right <= len(s):

            if right - left + 1 < len(t):
                if right == len(s):
                    break
                freqSubS[s[right]] += 1
                if s[right] in freqT and freqSubS[s[right]] == freqT[s[right]]:
                    have += 1
                right += 1
                continue

            if have == len(freqT):
                if res == "" or right - left < len(res):
                    res = s[left:right]
                if s[left] in freqT and freqSubS[s[left]] == freqT[s[left]]:
                    have -= 1
                freqSubS[s[left]] -= 1
                left += 1
            else:
                if right == len(s):
                    break
                freqSubS[s[right]] += 1
                if s[right] in freqT and freqSubS[s[right]] == freqT[s[right]]:
                    have += 1
                right += 1
        
        return res
