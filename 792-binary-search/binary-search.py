class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = (r + l+1) //2
        print(f"mid: {mid}")
        for num in nums:
            if nums[mid] == target:
                print(f"mid: {mid}")
                return mid
            elif nums[mid] < target:
                l = mid +1
                print(f"l: {l}")
            else:
                r = mid-1
                print(f"r: {r}")
            mid = (r + l) //2
        return -1
        


