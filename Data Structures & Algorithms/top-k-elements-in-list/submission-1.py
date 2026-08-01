class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = defaultdict(int)

        for n in nums:
            hashMap[n] += 1

        heap = []

        for n, c in hashMap.items():
            heapq.heappush(heap, (c, n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [n[1] for n in heap]
