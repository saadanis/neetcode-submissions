class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        tot = 1
        nz = 0

        for n in nums:
            if n == 0:
                nz += 1
                if nz > 1:
                    break
            else:
                tot *= n
        
        prods = []

        if nz == 0:
            for n in nums:
                prods.append(int(tot/n))
        elif nz == 1:
            for n in nums:
                if n == 0:
                    prods.append(tot)
                else:
                    prods.append(0)
        else:
            prods = [0] * len(nums)
        
        return prods
        