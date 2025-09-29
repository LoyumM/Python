# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.


class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stacks = []
        for idx in range(len(operations)):
            if operations[idx] == "C":
                stacks.pop()
            elif operations[idx] == "D":
                stacks.append(stacks[-1] * 2)
            elif operations[idx] == "+":
                stacks.append(stacks[-1] + stacks[-2])
            else:
                stacks.append(int(operations[idx]))
        return sum(stacks)

ops = ["5","2","C","D","+"]
# 30
solution = Solution()
print(solution.calPoints(ops))