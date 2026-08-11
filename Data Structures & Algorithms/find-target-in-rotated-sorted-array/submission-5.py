class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            center = start + (end - start) // 2

            if nums[center] == target:
                return center
            
            if nums[start] <= nums[center]:
                if target < nums[start] or target > nums[center]:
                    start = center + 1
                else:
                    end = center -1
            else:
                if target < nums[center] or target > nums[end]:
                    end = center - 1
                else:
                    start = center + 1

        return -1