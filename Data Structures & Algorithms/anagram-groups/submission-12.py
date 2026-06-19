class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        found = False
        
        for i in strs:
            if not result:
                result.append([i])
                continue
            for j in result:
                if sorted(j[0]) == sorted(i):
                    j.append(i)
                    found = True
            if not found:
                result.append([i])
            found = False
        print(result)
        
        return result
                
