def sumOfSquares(nums):
    total = 0
    n = len(nums)

    for i in range(n):
        distinct = set()

        for j in range(i, n):
            distinct.add(nums[j])
            count = len(distinct)
            total += count * count

    return total


nums = [1, 2, 1]
print(sumOfSquares(nums))