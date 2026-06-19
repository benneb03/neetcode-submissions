class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        total = 1

        i = 0
        j = 0

        while i < len(nums):
            for j in range(len(nums)):
                if i != j:
                    total = total * nums[j]
            result.append(total)
            i += 1
            total = 1
        
        return result