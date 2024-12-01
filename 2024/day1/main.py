def read_input(filepath: str) -> tuple[list, list]:
    left = []
    right = []

    with open(filepath, "r") as file:
        for line_number, line in enumerate(file, start=1):
            # Strip leading/trailing whitespace and split by any whitespace
            parts = line.strip().split()

            # Check if the line has at least two parts
            if len(parts) == 2:
                left.append(int(parts[0]))
                right.append(int(parts[1]))

    return left, right


def p1():
    l, r = read_input("./input.txt")
    sorted_l = sorted(l)
    sorted_r = sorted(r)
    total_diff = 0
    for i, num in enumerate(sorted_l):
        diff = abs(sorted_l[i] - sorted_r[i])
        total_diff += diff
    print(f"Result for part 1 is: {total_diff}")


def p2():
    l, r = read_input("./input.txt")
    sorted_l = sorted(l)
    sorted_r = sorted(r)
    count = {}
    similarity_score = 0
    for i, num in enumerate(sorted_r):
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for num in sorted_l:
        if num in count:
            similarity_score += num * (count[num])

    print(f"Result for part 2 is: {similarity_score}")


if __name__ == "__main__":
    p1()
    p2()
