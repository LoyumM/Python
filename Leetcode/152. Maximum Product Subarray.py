#time complexity O(n)2
def max_product(arr:list):
    n = len(arr)
    max_product_val = float('-inf')
    
    for i in range(n):
        current_product = 1
        
        for j in range(i, n):
            current_product *= arr[j]
            max_product_val = max(max_product_val, current_product)
            
    return max_product

nums = [2, 3, -2, 4]
print(max_product(nums))