class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}

        for i, n in enumerate(nums):
            hashMap[n] = i

        for i, n in enumerate(nums):

            diff = target - n

            if diff in hashMap and hashMap[diff] != i:
                return [i, hashMap[diff]]
