class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        print(words)
        reverse = words[::-1]
        print(reverse)
        reverse_words = " ".join(reverse)
        return(reverse_words)
        