from typing import List
class Codec:        
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # Encode by 5/Hello5/World
        result = ""
        for word in strs:
            result += str(len(word)) + "/" + word
        return result

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        i = 0
        while i < len(s):
            slash_index = s.index("/", i)
            length = int(s[i:slash_index])
            i = length+slash_index+1
            result.append(s[slash_index+1:i])
        return result



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))