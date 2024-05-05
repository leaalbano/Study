class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for index,value in enumerate(nums):
            difference = target - value
            if difference in visited:
                return[visited[difference], index]
            else:
                visited[value] = index