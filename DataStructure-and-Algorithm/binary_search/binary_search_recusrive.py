def binary_search(nums, target):
    return binary_search_recusrive(nums, target, 0, len(nums)-1)


def binary_search_recusrive(nums, target, low, high):
    if high < low:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return binary_search_recusrive(nums, target, low, mid - 1)
    else:
        return binary_search_recusrive(nums, target, mid + 1, high)
