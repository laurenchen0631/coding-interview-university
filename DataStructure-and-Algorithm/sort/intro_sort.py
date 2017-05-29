import math
from heap_sort import heap_sort_imp
from quick_sort import partition


def intro_sort(arr):
    # The factor two in the maximum depth is arbitrary;
    # it can be tuned for practical performance.
    max_depth = math.floor(math.log(len(arr))) * 2
    intro_sort_imp(arr, max_depth, 0, len(arr) - 1)


def intro_sort_imp(arr, max_depth, lo, hi):
    n = hi - lo + 1
    if n <= 1:
        return
    elif max_depth == 0:
        heap_sort_imp(arr, lo, hi)
    else:
        pivot = partition(arr, lo, hi)
        intro_sort_imp(arr, max_depth - 1, lo, pivot - 1)
        intro_sort_imp(arr, max_depth - 1, pivot + 1, hi)
