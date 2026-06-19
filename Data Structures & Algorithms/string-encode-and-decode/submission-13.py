class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result += str(len(i)) + "#" + i
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        word = []
        i = 0
        length = ""

        while i < len(s):
            while s[i] != "#":
                length += s[i]
                i += 1
                print(length)
            i += 1
            intlength = int(length)
            word = s[i:i+intlength]
            result.append(word)
            i += intlength
            length = ""
        
        return result
