def binary_search(nums, target):
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1
