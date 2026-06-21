class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l = 0
        r = len(s1) - 1
        s1 = "".join(sorted(s1))

        while r < len(s2):
            tmp = "".join(sorted(s2[l:r+1]))
            if tmp == s1:
                return True
            else:
                l+=1
                r+=1

        return False
