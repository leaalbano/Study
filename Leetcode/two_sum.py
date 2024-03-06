class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visitedNums = {}
        for i, value in enumerate(nums):
            difference = target - value
            if difference in visitedNums:
                return [visitedNums[difference], i]
            else:
                visitedNums[value] = i
                