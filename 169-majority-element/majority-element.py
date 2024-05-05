class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        greater_than = n/2
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num, value in count.items():
            if value > greater_than:
                return num
            
            

