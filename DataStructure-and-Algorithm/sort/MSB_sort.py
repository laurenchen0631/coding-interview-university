def radix_sort(arr):
    radix_sort_imp(arr, 0, 256)


def radix_sort_imp(a, i, k):
    if is_same_items(a):
        return

    buckets = [[] for _ in range(k)]
    for s in a:
        buckets[charAt(s, i)].append(s)

    count = 0
    for bucket in buckets:
        radix_sort_imp(bucket, i+1, k)
        for s in bucket:
            a[count] = s
            count += 1


def charAt(s, i):
    if i >= len(s):
        return 0  # ascii 0 means " "(space)
    else:
        return ord(s[i])


def is_same_items(a):
    if len(a) == 0:
        return True

    key = a[0]
    count = 0
    for item in a:
        if item == key:
            count += 1
    return count == len(a)
