class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        c = defaultdict(int)

        for n in nums:
            c[n] += 1

        res = []

        for i in range(len(nums)):
            c[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, len(nums)):
                c[nums[j]] -= 1
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = -(nums[i] + nums[j])
                if c[k] > 0:
                    res.append([nums[i], nums[j], k])
                
            for j in range(i + 1, len(nums)):
                c[nums[j]] += 1
            
        return res
        
        
