class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for char in s:
            if char in count:
                count[char] +=1
            else:
                count[char] = 1
                
        count2 = {}
        for c in t:
            if c in count2:
                count2[c] +=1
            else:
                count2[c] = 1
        
        if count == count2:
            return True
        return False
        