def parse_trees(line):
    ret = []

    for each in line:
        if each == ".":
            ret.append(False)
        elif each == "#":
            ret.append(True)
        else:
            raise Exception("Parsing Error")

    return ret


def count_trees(x_stride, y_stride, map):
    x = y = trees = 0

    while y < len(map):
        trees += int(map[y][x])

        x = (x + x_stride) % len(map[y])
        y = y + y_stride

    return trees


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = list(map(lambda x: parse_trees(x.strip()), f.readlines()))

    # p1
    print(count_trees(3, 1, lines))

    # p2
    print(
        count_trees(1, 1, lines)
        * count_trees(3, 1, lines)
        * count_trees(5, 1, lines)
        * count_trees(7, 1, lines)
        * count_trees(1, 2, lines)
    )
