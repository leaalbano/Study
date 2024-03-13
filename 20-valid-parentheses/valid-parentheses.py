class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #Initialize stack

        mapping = {"(": ")", "{": "}", "[": "]"}
        for c in s:
            if c in mapping:
                stack.append(c)
            elif len(stack) == 0 or c != mapping[stack.pop()]:
                return False
        if len(stack) == 0:
            return True
        else:
            return False


        