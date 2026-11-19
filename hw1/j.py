nums = [3, 5, 2, 8, 4, 6, 7, 9]
min_index = 0
max_index = 0
for i in range(len(nums)):
    if nums[i] < nums[min_index]:
        min_index = i
for x in range(len(nums)):
    if nums[x] > nums[max_index]:
        max_index = x
print(nums[max_index] - nums[min_index])

