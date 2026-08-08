class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break
            if i and n == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                uwu = n + nums[l] + nums[r]
                if uwu > 0:
                    r -= 1
                elif uwu < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res