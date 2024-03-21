class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        good_pairs = 0
        
        for i in range(0, len(nums), 1):
            for j in range(i+1, len(nums), 1):
                if nums[i] == nums[j]:
                    print(f"i: {i}, j: {j}")
                    good_pairs += 1
        return good_pairs


        