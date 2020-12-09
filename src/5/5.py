def parse_bin(str):
    def bin_str_to_num(str):
        ret = 0

        for each in str:
            ret <<= 1

            if each == "B" or each == "R":
                ret += 1

        return ret

    return bin_str_to_num(str[:7]), bin_str_to_num(str[7:])


def calc_seat_id(row, column):
    return row * 8 + column


def find_missing_seat(seats):
    for i in range(1, len(seats)):
        if seats[i] == seats[i - 1] + 2:
            return seats[i] - 1

    return None


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
        data = list(map(parse_bin, lines))

    seat_ids = list(map(lambda x: calc_seat_id(*x), data))

    # p1
    print(max(seat_ids))

    # p2
    seat_ids.sort()
    print(find_missing_seat(seat_ids))
