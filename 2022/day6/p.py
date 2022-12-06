from collections import deque
# open input.txt and read the entire file into a string
with open('input.txt', 'r') as f:
    data = f.read()

def part1():
    for x,y in enumerate(data):
        first, second, third, fourth = data[x], data[x+1], data[x+2], data[x+3]
        # check if all characters are different
        if first != second and first != third and first != fourth and second != third and second != fourth and third != fourth:
            print(x+3+1)
            break

def part2():
    for x,y in enumerate(data):
        current = data[x:x+14]
        if len(current) < 14:
            break
        # check if all characters are different
        if len(set(current)) == 14:
            print(x+14)
            break

part1()
part2()