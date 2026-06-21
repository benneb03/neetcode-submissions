class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        result = 0
        records = set()

        for r in range(len(s)):
            while s[r] in records:
                records.remove(s[l])
                l+=1
            records.add(s[r])
            result = max(result, r - l + 1)
        
        return result
