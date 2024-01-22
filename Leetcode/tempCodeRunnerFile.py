start, end = 0, 0
for end in range(len(nums)):
    if nums[end] == val:
        end += 1
    else: #nums[end] != val:
        nums[start],nums[end] = nums[end],nums[start]
        start += 1
        end += 1 