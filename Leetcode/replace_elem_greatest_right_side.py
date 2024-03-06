class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        greatest = 0
        replaced = [-1]
        for i in range(len(arr)-1, 0, -1):
            if arr[i] > greatest:
                greatest = arr[i]
            replaced.append(greatest)
        return reversed(replaced)
        