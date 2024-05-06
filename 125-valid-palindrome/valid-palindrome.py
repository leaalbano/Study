class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_string = ""
        for char in s:
            if char.isalnum():
                new_string += char
        final_string = new_string.lower()

        if final_string == final_string[::-1]:
            return True
        else:
            return False



            