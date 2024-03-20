class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = {}
        for char in magazine:
            if char in ransom:
                ransom[char] += 1
            else:
                ransom[char] = 1
        
        for ch in ransomNote:
            if ch in ransom and ransom[ch] > 0:
                ransom[ch] -= 1
            else:
                return False
        return True

        