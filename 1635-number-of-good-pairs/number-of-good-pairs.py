class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
 
        count = {}
        total = 0
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for val in count.items():
            c = val[1]*(val[1]-1) // 2
            total += c
        return total

        