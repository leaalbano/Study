class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for c in s: #original string
            if c.isalnum(): #alphanumeric char only
                newString = newString + c.lower() #add that char to the newString
        return newString == newString[::-1] #return if newstring is the same reversed