def jolt_diffs(nums):

    hm = {}

    for i, num in enumerate(nums):
        hm[num] = i

    jolts = 0
    ret = [0, 0, 1]  # 1, 2, 3 jolt differences

    while True:
        if jolts + 1 in hm:
            jolts += 1
            ret[0] += 1
        elif jolts + 2 in hm:
            jolts += 2
            ret[1] += 1
        elif jolts + 3 in hm:
            jolts += 3
            ret[2] += 1
        else:
            break
    return ret


def _jolt_diffs(nums, jolts, hm, memo):
    try:
        return memo[jolts]
    except KeyError:
        pass

    if jolts + 1 not in hm and jolts + 2 not in hm and jolts + 3 not in hm:
        memo[jolts] = 1
        return 1

    ret = 0
    if jolts + 1 in hm:
        ret += _jolt_diffs(nums, jolts + 1, hm, memo)
    if jolts + 2 in hm:
        ret += _jolt_diffs(nums, jolts + 2, hm, memo)
    if jolts + 3 in hm:
        ret += _jolt_diffs(nums, jolts + 3, hm, memo)
    memo[jolts] = ret
    return ret


def num_combinations(nums):
    hm = {}

    for i, num in enumerate(nums):
        hm[num] = i

    return _jolt_diffs(nums, 0, hm, {})


if __name__ == "__main__":
    with open("input.txt") as f:
        nums = list(map(lambda x: int(x.strip()), f.readlines()))

    # p1
    jds = jolt_diffs(nums)
    print(jds[0] * jds[2])

    # p2
    print(num_combinations(nums))
