class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)

        for n in nums:
            hashMap[n] += 1
        
        freqs = [[] for i in range(len(nums) + 1)]

        for n, c in hashMap.items():
            freqs[c].append(n)

        res = []

        for f in freqs[::-1]:
            for n in f:
                res.append(n)
                if len(res) == k:
                    return res