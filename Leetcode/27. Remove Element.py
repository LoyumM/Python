nums = [0,1,2,2,3,0,4,2]
val = 2

start, end = 0, 0
for end in range(len(nums)):
    if nums[end] == val:
        end += 1
    elif nums[end] != val:
        nums[start] = nums[end]
        nums[end] = val
        start += 1
        end += 1
        
print(nums)
