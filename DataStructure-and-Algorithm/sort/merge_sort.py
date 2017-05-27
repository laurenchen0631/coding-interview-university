from insertion_sort import insertion_sort_imp


def merge_sort_optimization(arr):
    # mergesort has too much overhead for tiny subarrays
    # if less than 7 items use insertion sort
    CUTOFF = 7

    def merge(a, aux, lo, mid, hi):
        i = lo
        j = mid + 1
        for k in range(lo, hi + 1):
            if i > mid:
                aux[k] = a[j]
                j += 1
            elif j > hi:
                aux[k] = a[i]
                i += 1
            elif a[j] < a[i]:
                aux[k] = a[j]
                j += 1
            else:
                aux[k] = a[i]
                i += 1

    def sort(a, aux, lo, hi):
        # if hi <= lo:
        #    return
        if hi <= lo + CUTOFF - 1:
            return insertion_sort_imp(a, lo, hi)
        mid = lo + (hi - lo)//2
        sort(aux, a, lo, mid)
        sort(aux, a, mid+1, hi)
        # stop when biggest item in left <= smallest item in right
        if aux[mid] <= aux[mid + 1]:
            return
        merge(aux, a, lo, mid, hi)

    aux = arr[:]
    sort(arr, aux, 0, len(arr) - 1)


def sort_recursive(a):
    # aux = [None] * len(a)
    sz = 1
    while sz < n:
        lo = 0
        while lo < len(a) - sz:
            merge(a, lo, lo+sz-1, min(lo+sz+sz-1, N - 1))
            lo += (sz + sz)
        sz = sz + sz


def merge_sort(arr):
    sort(arr, 0, len(arr) - 1)


def sort(arr, lo, hi):
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    sort(arr, lo, mid)
    sort(arr, mid+1, hi)
    merge(arr, lo, mid, hi)


def merge(arr, lo, mid, hi):

    # precondition: a[lo...mid] sorted
    assert(is_sorted(arr, lo, mid))
    # precondition: a[mid+1...hi] sorted
    assert(is_sorted(arr, mid + 1, hi))

    arr_copy = [arr[i] for i in range(lo, hi+1)]
    i = lo
    j = mid + 1
    for k in range(lo, hi+1):
        if mid < i:
            arr[k] = arr_copy[j-lo]
            j += 1
        elif hi < j:
            arr[k] = arr_copy[i-lo]
            i += 1
        elif arr_copy[i-lo] > arr_copy[j-lo]:
            arr[k] = arr_copy[j-lo]
            j += 1
        else:
            arr[k] = arr_copy[i-lo]
            i += 1

    # postcondition: arr[lo...hi] sorted
    assert(is_sorted(arr, lo, hi))


def is_sorted(arr, lo, hi):
    for i in range(lo, hi-1):
        if arr[i] > arr[i + 1]:
            return False
    return True
