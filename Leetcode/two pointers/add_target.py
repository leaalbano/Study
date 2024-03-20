'''Return True if there are two numbers that add up to target within list'''
nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13

left = 0
right = len(nums)-1

while left < right:
    if nums[right] + nums[left] > target:
        right -= 1