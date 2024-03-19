# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            middle = (left + right) // 2
            print(f"left {left}")
            print(f"right {right}")
            print(f"middle {middle}")

            if isBadVersion(middle):
                right = middle - 1
                print(f"new right:{right}")
            else:
                left = middle + 1
                print(f"new left:{left}")
        return left

        