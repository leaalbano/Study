class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        l_position, r_position = -1, -1
        min_distance = len(wordsDict)

        for index, word in enumerate(wordsDict, start = 1):
            if word == word1:
                l_position = index
                print(f"l: {l_position}")
            elif word == word2:
                r_position = index
                print(f"r: {r_position}")
            if l_position != -1 and r_position != -1:
                min_distance = min(min_distance, abs(l_position - r_position))
        print(f"min: {min_distance}")
        return min_distance

