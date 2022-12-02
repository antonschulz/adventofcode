# read input from input.txt which looks like this: B Z and store each line in a list
with open('input.txt') as f:
    content = f.readlines()
# remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

def part1():
    score = 0
    for x in content:
        x = list(x)
        user = {'X': 1, 'Y': 2, 'Z': 3}
        score += user[x[2]]
        if x[0] == 'A':
            if x[2] == 'X':
                score += 3
            elif x[2] == 'Y':
                score += 6
        if x[0] == 'B':
            if x[2] == 'Y':
                score += 3
            elif x[2] == 'Z':
                score += 6
        if x[0] == 'C':
            if x[2] == 'Z':
                score += 3
            elif x[2] == 'X':
                score += 6
    print(score)


def part2():
    score = 0
    for x in content:
        x = list(x)
        user = {'X': 1, 'Y': 2, 'Z': 3}
        if x[0] == 'A':
            if x[2] == 'X':
                score += 0
                choice = 'Z'
            elif x[2] == 'Y':
                score += 3
                choice = 'X'
            elif x[2] == 'Z':
                score += 6
                choice = 'Y'
        if x[0] == 'B':
            if x[2] == 'X':
                score += 0
                choice = 'X'
            elif x[2] == 'Y':
                score += 3
                choice = 'Y'
            elif x[2] == 'Z':
                score += 6
                choice = 'Z'
        if x[0] == 'C':
            if x[2] == 'X':
                score += 0
                choice = 'Y'
            elif x[2] == 'Y':
                score += 3
                choice = 'Z'
            elif x[2] == 'Z':
                score += 6
                choice = 'X'
        score += user[choice]
    print(score)




part1()
part2()

