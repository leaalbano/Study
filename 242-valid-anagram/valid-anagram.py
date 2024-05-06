class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}
        for letter in s:
            if letter in s_count:
                s_count[letter] += 1
            else:
                s_count[letter] = 1
        
        for char in t:
            if char in t_count:
                t_count[char] += 1
            else:
                t_count[char] = 1
        
        if s_count == t_count:
            return True
        else:
            return False

