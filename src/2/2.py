def split(str, delims):
    ret = []
    cur = ""

    for i in range(len(str)):
        if str[i] in delims:
            if cur != "":
                ret.append(cur)
                cur = ""
        else:
            cur += str[i]
        i += 1

    if cur != "":
        ret.append(cur)

    return ret


def is_valid1(min, max, char, password):
    c = 0

    for each in password:
        if each == char:
            c += 1

    return c >= min and c <= max


def is_valid2(min, max, char, password):
    a = b = False

    try:
        a = (password[min - 1] == char)
        b = (password[max - 1] == char)
    except IndexError:
        pass

    return a ^ b


def p1(data):
    return sum(list(map(lambda x: is_valid1(**x), data)))


def p2(data):
    return sum(list(map(lambda x: is_valid2(**x), data)))


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = list(map(lambda x: split(x.strip(), "-: "), f.readlines()))
        data = list(
            map(
                lambda x: {
                    "min": int(x[0]),
                    "max": int(x[1]),
                    "char": x[2],
                    "password": x[3],
                },
                lines,
            )
        )

    print(p1(data))

    print(p2(data))
