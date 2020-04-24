def quickSort(nums): return nums if len(nums) < 2 else quickSort([i for i in nums[1:] if i < nums[0]]) +\
    [nums[0]]+quickSort([c for c in nums[1:] if c >= nums[0]])


nums = [1, 4, 5, 2, 1, 1, 2, 1, 3]
print(quickSort(nums))
