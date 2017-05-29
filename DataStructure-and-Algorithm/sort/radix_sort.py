# radix sort used when len(buckets) >>> len(nums)
def radix_sort(nums, base=10):
    buckets = [[] for _ in range(base)]

    for level in range(get_num_digits(max(nums), base)):
        for num in nums:
            radix = get_kth_digit(num, level+1, base)
            buckets[radix].append(num)

        i = 0
        for bucket in buckets:
            for num in bucket:
                nums[i] = num
                i += 1
            bucket.clear()


def get_kth_digit(num, k, base):
    for _ in range(k - 1):
        num //= base
    return num % base


def get_num_digits(num, base):
    count = 0
    while num != 0:
        num //= base
        count += 1
    return count


if __name__ == "__main__":
    x = [720, 450, 771, 922, 352, 504, 905, 5, 955, 825, 777, 858, 28, 829]
    radix_sort(x)
    print(x)
