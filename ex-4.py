def countPairs(nums, k):
    groups = {}
    count = 0

    for i in range(len(nums)):
        if nums[i] not in groups:
            groups[nums[i]] = []

        for j in groups[nums[i]]:
            if (i * j) % k == 0:
                count += 1

        groups[nums[i]].append(i)

    return count


nums = [3, 1, 2, 2, 2, 1, 3]
k = 2

print(countPairs(nums, k))