def removeDuplicates(nums: list[int]):
    k = 0
    for idx, val in enumerate(nums):
        print(f"new loop {nums}")
        if k < 2 or val != nums[k - 2]:
            print(f"during the loop {nums}")
            print(f"k {k}, idx {idx}, nums[k - 2] {nums[k - 2]}, val {val}")
            nums[k] = val
            print(f"swapped {nums}")
            k += 1
            print(f"k {k}, idx {idx}, nums[k - 2] {nums[k - 2]}, val {val}")
    print(nums)
    return k 

# nums = [1,1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums))