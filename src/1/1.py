def part1(lines, target):
    hs = {}

    for i, each in enumerate(lines):
        complement = target - each

        try:
            complement_index = hs[complement]
            return complement * each
        except KeyError:
            hs[each] = i


def part2(lines, target):

    lines.sort()

    for i in range(len(lines)):
        j = i + 1
        k = len(lines) - 1

        while j < k:
            s = lines[i] + lines[j] + lines[k]
            if s == target:
                return lines[i] * lines[j] * lines[k]
            elif s < target:
                j += 1
            else:
                k -= 1


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = list(map(lambda x: int(x.strip()), f.readlines()))

    target = 2020
    print(part1(lines, target))

    print(part2(lines, target))
