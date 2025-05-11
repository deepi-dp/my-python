def twoSum(nums, target):
    size = len(nums)
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            print(nums[i], nums[j])
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [2, 7, 11, 15]
#       0  1   2   3
target = 9

print(twoSum(nums, target))
