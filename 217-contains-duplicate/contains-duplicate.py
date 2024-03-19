class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = set()

        for num in nums:
            if num in mp:
                return True
            else:
                mp.add(num)
        return False