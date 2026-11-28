class Solution:
    '''
    s = "abc"

    # Character to ASCII/Unicode code point
    print(ord('a'))  # 97

    # ASCII/Unicode code point to character
    print(chr(97))   # a

    # Character comparison
    print('a' < 'b') # True

    s = "abc123def456"

    result = ''.join(char for char in s if not char.isdigit())

    print(result)
    '''
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
    
        return result

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != "#":
                j+=1
            size = int(s[i:j])
            i = j+1
            j = i+size
            res.append(s[i:j])
            i = j
        return res
        
