def read_input(filepath: str) -> tuple[list, list]:
    reports = []
    with open(filepath, "r") as file:
        for line_number, line in enumerate(file, start=1):
            # Strip leading/trailing whitespace and split by any whitespace
            line = line.strip().split()
            reports.append([int(x) for x in line])
            # Check if the line has at least two parts

    return reports


def valid_level(one: int, two: int, inc: bool) -> bool:
    diff = two - one
    if diff == 0 or abs(diff) > 3:
        return False
    else:
        if inc and two > one:
            return True
        elif not inc and two < one:
            return True
        else:
            return False


def valid_report(report: list) -> bool:
    tuples = zip(report, report[1:])
    first = report

    if first[1] < first[0]:
        inc = False
    else:
        inc = True

    for tuple in tuples:
        if valid_level(tuple[0], tuple[1], inc):
            continue
        else:
            return False
    return True


def p1(filepath: str):
    input = read_input(filepath)

    true_count = 0
    for report in input:
        if valid_report(report):
            true_count += 1

    print(f"Result for part 1: {true_count}")


def get_diff_list(report: list) -> list:
    zipped = zip(report, report[1:], report[2:])

    return zipped


def valid_level_p2(diff_list: list) -> bool:
    


def p2(filepath: str):
    input = read_input(filepath)
    for report in input:
        diff_list = get_diff_list(report)
        valid_level_p2(diff_list)


if __name__ == "__main__":
    filepath = "./example.txt"
    p1(filepath)
    p2(filepath)
