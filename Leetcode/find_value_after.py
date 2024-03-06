class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        increment = ['++X', 'X++']
        decrement = ['--X', 'X--']
        x = 0
        for value in operations:
            if value in increment:
                x += 1
            else:
                x -= 1
        print(x)
        return x

        