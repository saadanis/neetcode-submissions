class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while True:
            center = (end - start) // 2 + start

            if nums[center] <= nums[(center - 1) % len(nums)] and nums[center] <= nums[(center + 1) % len(nums)]:
                return nums[center]
            
            if nums[center] > nums[end]:
                start = center + 1
            else:
                end = center
        
