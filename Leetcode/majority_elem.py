class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        values = {}
        for num in nums:
            if num in values:
                values[num] += 1
                print(values)
            else:
                values[num] = 1
                print(values)

        most = len(nums) // 2
        for num, value in values.items():
            if value > most:
                return num
