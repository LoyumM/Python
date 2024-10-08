# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = {char: i for i, char in enumerate(jewels)}
        count = 0
        for j in stones:
            if j in d:
                count += 1
        return count

jewels = "aA"
stones = "aaAbhsh"
#expected_output = 3
instance = Solution()
print(instance.numJewelsInStones(jewels, stones))
