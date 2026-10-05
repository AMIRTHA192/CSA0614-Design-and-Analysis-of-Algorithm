def findCounts(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    answer1 = 0
    answer2 = 0

    for x in nums1:
        if x in set2:
            answer1 += 1

    for x in nums2:
        if x in set1:
            answer2 += 1

    return [answer1, answer2]


nums1 = [2, 3, 2]
nums2 = [1, 2]

print(findCounts(nums1, nums2))