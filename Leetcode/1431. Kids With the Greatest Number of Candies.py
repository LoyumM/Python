class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        res = []
        for candy in candies:
            if candy + extraCandies >= max(candies):
                res.append(True)
            else:
                res.append(False)
        return res
        

candies = [2,3,5,1,3]
extraCandies = 3
#expected_output: [true,true,true,false,true] 
solution = Solution()
print(solution.kidsWithCandies(candies, extraCandies))