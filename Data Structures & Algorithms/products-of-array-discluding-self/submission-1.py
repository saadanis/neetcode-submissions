class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        pref = [1] + [0] * (n - 1)
        suff = [0] * (n - 1) + [1]
        ress = [0] * n

        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]
        for i in range(n):
            ress[i] = pref[i] * suff[i]
        
        return ress