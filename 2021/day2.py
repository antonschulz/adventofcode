
data = open("input.txt", "r")

data = data.read().split("\n")
# part 1
depth = 0
horizontal = 0
for line in data:
    match line.split(" "):
        case ["forward", num]:
            horizontal += int(num)
        case ["down", num]:
            depth += int(num)
        case ["up", num]:
            depth -= int(num)

print("Part 1: ",depth * horizontal)

# part 2
aim = 0
depth = 0
horizontal = 0
for line in data:
    match line.split(" "):
        case ["forward", num]:
            horizontal += int(num)
            depth += aim * int(num)
        case ["down", num]:
            aim += int(num)
        case ["up", num]:
            aim -= int(num)


print("Part 2: ",depth * horizontal)
    

