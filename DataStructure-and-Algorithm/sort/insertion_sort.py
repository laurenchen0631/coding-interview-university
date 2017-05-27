def insertion_sort(arr):
    insertion_sort_imp(arr, 0, len(arr) - 1)


def insertion_sort_imp(a, lo, hi):
    for i in range(lo, hi+1):
        j = i
        while j > 0 and a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
            j -= 1
