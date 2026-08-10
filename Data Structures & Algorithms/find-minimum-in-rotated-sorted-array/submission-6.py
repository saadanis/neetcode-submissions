class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start < end:

            center = (end - start) // 2 + start
            
            if nums[center] > nums[end]:
                start = center + 1
            else:
                end = center
        
        return nums[start]
        
