#time complexity O(n2)
def max_product(arr:list):
    n = len(arr)
    max_product_val = float('-inf')
    
    for i in range(n):
        current_product = 1
        
        for j in range(i, n):
            current_product *= arr[j]
            max_product_val = max(max_product_val, current_product)
            
    return max_product

# nums = [2, 3, -2, 4]
# print(max_product(nums))

#time complexity O(n)
class Solution:
    def maxProduct(self, nums: list):
        res = max(nums)

        curMax, curMin = 1,1

        for num in nums:
            tmp = curMax * num
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(tmp, curMin * num, num)
            res = max(res, curMax)

        return res

nums = [2, 3, -2, 4]

solution_instance = Solution()

result = solution_instance.maxProduct(nums)

print(result)