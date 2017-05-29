def insertion_sort(arr):
    insertion_sort_imp(arr, 0, len(arr) - 1)


def insertion_sort_imp(a, lo, hi):
    for i in range(lo, hi+1):
        j = i
        while j > lo and a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]  # move a[j] to previous slot
            j -= 1  # a[j] will be in a[j-1]
