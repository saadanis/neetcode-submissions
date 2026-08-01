class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = defaultdict(int)

        for n in nums:
            hashMap[n] += 1

        arr = []

        for n, f in hashMap.items():
            arr.append([f, n])
        
        arr.sort()

        return [a[1] for a in arr[len(arr)-k:]]