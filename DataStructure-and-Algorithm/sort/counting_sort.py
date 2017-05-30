def counting_sort(nums):
    if not len(nums):
        return
    bucket = max(nums)
    counts = [0] * bucket
    for num in nums:
        count[num] += 1

    total = 0
    for (i, count) in enumerate(counts):
        counts[i] = total
        total += count

    # keep sorted items stable
    aux = [None] * len(nums)
    for num in nums:
        aux[counts[num]] = num
        counts[num] += 1

    # put it back
    for i in range(len(nums)):
        nums[i] = aux[i]
