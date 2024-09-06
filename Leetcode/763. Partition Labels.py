# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occurance = {char:idx for idx,char in enumerate(s)}
        result = []
        start, end = 0,0
        for idx, char in enumerate(s):
            #updating the end of current partition
            end = max(end, last_occurance[char])

            #record the end of the partition
            if idx == end:
                result.append(end - start + 1)
                start = idx + 1

        return result


s = "ababcbacadefegdehijhklij"
#expectedOutput: [9,7,8]
#Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
solution = Solution()
print(solution.partitionLabels(s))