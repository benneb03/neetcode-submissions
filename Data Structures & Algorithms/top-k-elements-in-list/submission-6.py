class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        result = []

        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        
        for j in range(k):
            highest = max(dict, key=dict.get)
            result.append(highest)
            del dict[highest]
        
        return result