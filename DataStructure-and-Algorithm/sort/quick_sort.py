import random
from insertion_sort import insertion_sort_imp


# Worst case: 0.5N^2
# Avreage case: 1.39 N*lg(N)
def quick_sort(arr):
    # shuffle is needed for performance guarantee
    random.shuffle(arr)
    sort(arr, 0, len(arr) - 1)


# select the kth largest item in unsorted array
# average case: O(N)
def select_sort(arr, k):
    arr = arr[:]
    random.shuffle(arr)
    lo = 0
    hi = len(arr) - 1
    while lo < hi:
        j = partition(arr, lo, hi)
        if j < k:
            lo = j + 1
        elif k < j:
            hi = j - 1
        else:
            return arr[k]
    return arr[k]


def partition(a, lo, hi):
    i = lo + 1
    j = hi
    while i <= j:
        if a[i] <= a[lo]:
            i += 1
        elif a[j] > a[lo]:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
    a[lo], a[j] = a[j], a[lo]
    return j


def three_way_partition(a, lo, hi):
    lt = lo
    gt = hi
    v = a[lo]
    i = lo
    while i <= gt:
        if a[i] < v:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif a[i] > v:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1
    return (lt, gt)


def sort(arr, lo, hi):
    CUTOFF = 10
    if hi <= lo + CUTOFF - 1:
        insertion_sort_imp(arr, lo, hi)
        return

    median = median_of_three(arr, lo, lo + (hi - lo)//2, hi)
    if median != lo:
        arr[lo], arr[median] = arr[median], arr[lo]

    # p = partition(arr, lo, hi)
    # sort(arr, lo, p - 1)
    # sort(arr, p + 1, hi)
    (lt, gt) = three_way_partition(arr, lo, hi)
    sort(arr, lo, lt - 1)
    sort(arr, gt + 1, hi)


def median_of_three(arr, lo, mid, hi):
    nums = [lo, mid, hi]
    insertion_sort_imp(nums, 0, 2)
    return nums[1]
