

# Use 2NlgN character compares on average for random string
# Avoids re-comparing long common prefixes
def quicksort(arr):
    if type(arr[0]) is not str:
        raise TypeError("3-way quicksort can only be used in [str]")
    quicksort_imp(arr, 0, len(a - 1), 0)


def quicksort_imp(a, lo, hi, level):
    if hi <= lo:
        return

    lt = lo
    gt = hi
    i = lo + 1
    pivot = charAt(a[lo], level)
    while i <= gt:
        c = charAt(a[i], level)
        if c < pivot:
            a[i], a[lt] = a[lt], a[i]
            i += 1
            lt += 1
        elif c > pivot:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1
    quicksort_imp(a, lo, lt-1, level)
    if v != 0:
        quicksort_imp(a, lt, gt, level+1)
    quicksort_imp(a, gt+1, hi, level)


def charAt(s, i):
    if len(s) <= i:
        return 0
    return s[i]
