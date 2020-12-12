dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]


def num_occupied(seats):
    return sum(map(lambda i: sum(map(lambda j: int(j == "#"), i)), seats))


def _count(seats, x, y):
    if y >= 0 and y < len(seats) and x >= 0 and x < len(seats[y]):
        return seats[y][x] == "#"
    return False


def count_adjacent(seats, x, y):
    return sum([_count(seats, x + dx, y + dy) for dx, dy in dirs])


def run_round(seats):
    ret = [x.copy() for x in seats]
    changes = 0

    for y in range(len(seats)):
        for x in range(len(seats[y])):
            if seats[y][x] == ".":
                continue

            adj = count_adjacent(seats, x, y)

            if seats[y][x] == "#" and adj >= 4:
                ret[y][x] = "L"
                changes += 1
            elif seats[y][x] == "L" and adj == 0:
                ret[y][x] = "#"
                changes += 1

    return ret, changes


def _count2(seats, x, y):
    if y >= 0 and y < len(seats) and x >= 0 and x < len(seats[y]):
        return seats[y][x] != ".", seats[y][x] == "#"
    return True, False


def count_adjacent2(seats, x, y):
    count = 0

    for dx, dy in dirs:
        new_x = x
        new_y = y
        seat_found = False
        while not seat_found:
            new_x += dx
            new_y += dy
            seat_found, occupied = _count2(seats, new_x, new_y)
        count += int(occupied)

    return count


def run_round2(seats):
    ret = [x.copy() for x in seats]
    changes = 0

    for y in range(len(seats)):
        for x in range(len(seats[y])):
            if seats[y][x] == ".":
                continue

            adj = count_adjacent2(seats, x, y)

            if seats[y][x] == "#" and adj >= 5:
                ret[y][x] = "L"
                changes += 1
            elif seats[y][x] == "L" and adj == 0:
                ret[y][x] = "#"
                changes += 1

    return ret, changes


if __name__ == "__main__":
    with open("input.txt") as f:
        seats = list(map(lambda x: list(x.strip()), f.readlines()))
        seats2 = [x.copy() for x in seats]

    # p1
    changes = 1
    while changes != 0:
        seats, changes = run_round(seats)

    print(num_occupied(seats))

    # p2
    changes = 1
    seats = seats2
    while changes != 0:
        seats, changes = run_round2(seats)

    print(num_occupied(seats))
