class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        res = 0

        for n in nums:
            if not hashMap[n]:
                hashMap[n] = hashMap[n - 1] + hashMap[n + 1] + 1
                hashMap[n - hashMap[n - 1]] = hashMap[n]
                hashMap[n + hashMap[n + 1]] = hashMap[n]
                res = max(res, hashMap[n])
        
        return res