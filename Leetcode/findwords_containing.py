class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # answer = []
        # index = 0
        # for word in words:
        #     if x in word:
        #         answer.append(index)
        #     index += 1
        # return answer
        answer = []
        for i, word in enumerate(words):
            if x in word:
                answer.append(i)
        return answer
      