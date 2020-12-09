def xmas(nums, i):
    assert i > 24

    n = nums[i]

    hs = {}

    c = i - 25
    while c < i:
        v = nums[c]
        try:
            hs[n - v]
            return True
        except KeyError:
            hs[v] = 1
        c += 1

    return False


# p1
def find_invalid(nums):
    i = 25
    while i < len(nums):
        if not xmas(nums, i):
            return i, nums[i]
        i += 1


# p2
def find_contiguous(nums, value):
    i = 0
    while i < len(nums):
        j = i + 1
        s = nums[i]
        while j < len(nums):
            s += nums[j]
            if s == value:
                return i, j
            elif s > value:
                break
            j += 1
        i += 1
    return None


if __name__ == "__main__":
    with open("input.txt") as f:
        nums = list(map(lambda x: int(x.strip()), f.readlines()))

    first_invalid = find_invalid(nums)[1]
    print(first_invalid)

    start, stop = find_contiguous(nums, first_invalid)
    print(min(nums[start : stop + 1]) + max(nums[start : stop + 1]))
