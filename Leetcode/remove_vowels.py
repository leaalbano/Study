class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        new_string = ""
        for letter in range(len(s)):
            if s[letter] in vowels:
                continue
            else:
                new_string += s[letter]
        print(new_string)
        return new_string

        