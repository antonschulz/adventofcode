import itertools


def read_input(filename):
    with open(filename, "r") as file:
        file_content = file.read()
    return file_content


def p1(input):
    valid = []
    for key, val in input.items():

        operators = list(itertools.product(range(2), repeat=len(val) - 1))
        for operator_perm in operators:
            _sum = 1 * val[0]
            for i, value in enumerate(val[1:]):
                if operator_perm[i] == 0:
                    _sum += value
                if operator_perm[i] == 1:
                    _sum *= value
            if _sum == key:
                valid.append(key)
                break
    print(sum(valid))


def p2(input):
    valid = []
    for key, val in input.items():

        operators = list(itertools.product(range(3), repeat=len(val) - 1))
        for operator_perm in operators:
            _sum = 1 * val[0]
            for i, value in enumerate(val[1:]):
                if operator_perm[i] == 0:
                    _sum += value
                if operator_perm[i] == 1:
                    _sum *= value
                if operator_perm[i] == 2:
                    concat = str(_sum) + str(value)
                    _sum = int(concat)
            if _sum == key:
                valid.append(key)
                break
    print(sum(valid))


if __name__ == "__main__":
    path = "2024/day7/"
    input = read_input(path + "input.txt")
    split_input = input.split("\n")
    d = {}
    for line in split_input:
        vals = [x.replace(":", "") for x in line.split(" ")]
        if len(vals) > 1:
            d[int(vals[0])] = [int(x) for x in vals[1:]]
    p1(d)
    p2(d)
