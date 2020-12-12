dirs = ["N", "E", "S", "W"]


def parse_line(line):
    return (line[0], int(line[1:]))


def manhattan_distance(data):
    return sum(map(abs, data))


def move(loc, d, m):
    if d == "N":
        loc[0] += m
    elif d == "E":
        loc[1] += m
    elif d == "S":
        loc[0] -= m
    elif d == "W":
        loc[1] -= m
    else:
        raise ValueError


def travel(route, loc=[0, 0], f=1):
    for d, m in route:
        if d in dirs:
            move(loc, d, m)
        elif d == "R":
            f = (f + (m // 90)) % len(dirs)
        elif d == "L":
            f = (f - (m // 90)) % len(dirs)
        elif d == "F":
            move(loc, dirs[f], m)
        else:
            raise ValueError

    return loc


def rotate(data, amount, clockwise=True):
    if not clockwise:
        amount = 4 - amount

    for _ in range(amount):
        temp = data[1]
        data[1] = data[0]
        data[0] = -temp


def travel2(route, waypoint=[1, 10], loc=[0, 0]):
    for d, m in route:
        if d in dirs:
            move(waypoint, d, m)
        elif d == "R" or d == "L":
            rotate(waypoint, m // 90, d == "R")
        elif d == "F":
            loc[0] += waypoint[0] * m
            loc[1] += waypoint[1] * m
        else:
            raise ValueError
        print(d, m, waypoint, loc)

    return loc


if __name__ == "__main__":
    with open("input.txt") as f:
        data = list(map(lambda x: parse_line(x.strip()), f.readlines()))

    # p1
    end_loc = travel(data)
    print(manhattan_distance(end_loc))

    # p2
    end_loc = travel2(data)
    print(end_loc)
    print(manhattan_distance(end_loc))
