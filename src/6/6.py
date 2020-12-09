class Group:
    def __init__(self):
        self.group = {}
        self.size = 0

    def add_answer(self, char):
        try:
            self.group[char] += 1
        except KeyError:
            self.group[char] = 1

    def add_member(self):
        self.size += 1

    def num_anyone(self):
        return len(self.group.keys())

    def num_everyone(self):
        return sum([value == self.size for value in self.group.values()])


def build_groups(lines):
    ret = []

    group = Group()

    for line in lines:
        if len(line) == 0:
            ret.append(group)
            group = Group()
            continue

        group.add_member()
        for char in line:
            group.add_answer(char)

    ret.append(group)
    return ret


def count_group(group):
    return len(group.keys())


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
        data = build_groups(lines)

    # p1
    print(sum(map(lambda x: x.num_anyone(), data)))

    # p2
    print(sum(map(lambda x: x.num_everyone(), data)))
