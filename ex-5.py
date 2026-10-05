def findLargest(nums):
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    return largest


print(findLargest([1, 2, 3, 4, 5]))
print(findLargest([7, 7, 7, 7, 7]))
print(findLargest([-10, 2, 3, -4, 5]))