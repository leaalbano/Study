class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        original = {}
        for num in nums:
            if num not in original:
                original[num] = 1
            elif num in original:
                original[num] += 1
                if original[num] >= 2:
                    return True
        return False
        