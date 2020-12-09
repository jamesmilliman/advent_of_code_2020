def parse_instruction(line):
    instr = line[:3]
    numb = int(line[5:])
    neg = line[4] == "-"

    if neg:
        numb *= -1

    return [instr, numb]


def run(instrs):
    acc = 0
    visited = [False for _ in range(len(instrs))]

    i = 0
    while i < len(instrs) and not visited[i]:
        visited[i] = True
        instr, num = instrs[i]

        if instr == "nop":
            i += 1
        elif instr == "acc":
            i += 1
            acc += num
        elif instr == "jmp":
            i += num
        else:
            raise ValueError()

    return i >= len(instrs), acc


def _flip(instr):
    if instr[0] == "nop":
        instr[0] = "jmp"
    elif instr[0] == "jmp":
        instr[0] = "nop"


def fix(instrs):
    i = 0
    while i < len(instrs):
        if instrs[i][0] == "nop" or instrs[i][0] == "jmp":
            _flip(instrs[i])
            succeeded, acc = run(instrs)
            if succeeded:
                return acc
            _flip(instrs[i])

        i += 1
    return None


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
        data = list(map(parse_instruction, lines))

    # p1
    print(run(data))

    # p2
    print(fix(data))
