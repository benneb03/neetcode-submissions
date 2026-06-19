class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numbers = set(nums)
        longest = 0

        for i in numbers:
            if (i - 1) not in numbers:
                length = 1
                while (i + length) in numbers:
                    length += 1
                if length > longest:
                    longest = length
        return longest
        