from statistics import median
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_array = []
        unsorted = []

        unsorted.extend(nums1)
        print(unsorted)
        unsorted.extend(nums2)
        print(unsorted)
        sorted_array = sorted(unsorted)
        print(sorted_array)
        if len(sorted_array)%2 == 0:
            print(len(sorted_array))
            middle = len(sorted_array)//2
            print(f"middle: {middle}")
            next_num = middle-1
            print(f"next num: {next_num}")
            total = sorted_array[middle]+sorted_array[next_num]
            print(f"total {total}")
            avg = total / 2
            print(f"avg {avg}")
            return avg
        else:
            median_value = median(sorted_array)
            print(median_value)
            return median_value