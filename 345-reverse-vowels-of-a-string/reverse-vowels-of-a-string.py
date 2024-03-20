class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s)-1
        array = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
        while i<j:
            if array[i] not in vowels:
                i += 1
            elif array[j] not in vowels:
                j -= 1
            elif array[i] and array[j] in vowels:
                array[i], array[j] = array[j], array[i]
                i+=1
                j-=1
        return ''.join(array)
