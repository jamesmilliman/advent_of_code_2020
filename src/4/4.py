def parse_text(data):
    slow = fast = lineend = semicolon = 0

    ret = list()
    entry = dict()
    while fast < len(data):
        # print(data[fast])
        if data[fast] == "\n":
            if lineend == (fast - 1):
                ret.append(entry)
                entry = dict()
            else:
                entry[data[slow:semicolon]] = data[semicolon + 1 : fast]

            slow = fast + 1
            lineend = fast
        elif data[fast] == " ":
            if fast != slow:
                entry[data[slow:semicolon]] = data[semicolon + 1 : fast]
            slow = fast + 1
        elif data[fast] == ":":
            semicolon = fast

        fast += 1

    return ret


REQUIRED_VALUES = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
VALID_EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
zero_ord = ord("0")
nine_ord = ord("9")
a_ord = ord("a")
f_ord = ord("f")

# writing my own for practice
def is_numeric(v):
    if isinstance(v, str):
        v = ord(v[0])

    return zero_ord <= v and v <= nine_ord


def is_hex(v):
    if isinstance(v, str):
        v = ord(v[0])

    return is_numeric(v) or (a_ord <= v and v <= f_ord)


def parse_numeric_and_suffix(s):
    numeric = None
    suffix = ""

    i = 0
    while i < len(s):
        o = ord(s[i])
        if o >= zero_ord and o <= nine_ord:
            if numeric is None:
                numeric = o - zero_ord
            else:
                numeric *= 10
                numeric += o - zero_ord
        else:
            break

        i += 1

    assert numeric is not None
    return numeric, s[i:]


def is_valid1(entry):
    return all([each in entry for each in REQUIRED_VALUES])


def validate(key, value):
    if key == "byr":
        value = int(value)
        return value > 1919 and value < 2003
    elif key == "iyr":
        value = int(value)
        return value > 2009 and value < 2021
    elif key == "eyr":
        value = int(value)
        return value > 2019 and value < 2031
    elif key == "hgt":
        numeric, suffix = parse_numeric_and_suffix(value)

        if suffix == "cm":
            return numeric > 149 and numeric < 194
        elif suffix == "in":
            return numeric > 58 and numeric < 77
        else:
            return False
    elif key == "hcl":
        if len(value) != 7 or value[0] != "#":
            return False

        return all(map(is_hex, value[1:]))
    elif key == "ecl":
        return value in VALID_EYE_COLORS
    elif key == "pid":
        return len(value) == 9 and all(map(is_numeric, value))

    return False


def is_valid2(entry):
    return all(
        [(each in entry) and validate(each, entry[each]) for each in REQUIRED_VALUES]
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        data = parse_text(f.read())

    # p1
    print(sum(map(is_valid1, data)))

    # p2
    print(sum(map(is_valid2, data)))
