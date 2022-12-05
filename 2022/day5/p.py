import re

with open('input.txt') as f:
    data = f.read()
    instructions = data.split('\n\n')[1]
    stacks = data.split('\n\n')[0].split('\n')


# each character takes up two spaces and is followed by a space
dic = {}
for line in stacks:
    depth = 0
    length = len(line)
    step = 4
    for i in range(1, length, step):
        try:
            dic[i-(depth*3)].append(line[i])
        except:
            dic[i-(depth*3)] = []
            dic[i-(depth*3)].append(line[i])
        depth += 1

# {1: [' ', 'N', 'Z', '1'], 2: ['D', 'C', 'M', '2'], 3: [' ', ' ', 'P', '3']}
newdic = {}
for key in dic:
    for val in dic[key]:
        if val != ' ':
            try:
                newdic[key].append(val)
            except:
                newdic[key] = []
                newdic[key].append(val)
# {1: [' ', 'N', 'Z', '1'], 2: ['D', 'C', 'M', '2'], 3: [' ', ' ', 'P', '3']}
def move(amount, f, t):
    for x in range(0, amount):
        value = newdic[f][0]
        del newdic[f][x]
        newdic[t].insert(0, value)

def part1():
    i = instructions.split('\n')
    for instruction in i:
        # write a regex that finds all numbers in the instruction
        amount, f, t = re.findall(r'\d+', instruction)
        move(int(amount), int(f), int(t))
    ans = ""
    for key in newdic:
        ans += newdic[key][0]
    print(ans)

def move2(amount, f, t):
    for x in range(amount, 0, -1):
        value = newdic[f][x-1]
        del newdic[f][x-1]
        newdic[t].insert(0, value)

def part2():
    i = instructions.split('\n')
    for instruction in i:
        # write a regex that finds all numbers in the instruction
        amount, f, t = re.findall(r'\d+', instruction)
        if int(amount) == 1:
            move(int(amount), int(f), int(t))
        else: move2(int(amount), int(f), int(t))
    ans = ""
    for key in newdic:
        ans += newdic[key][0]
    print(ans)


#part1()
part2()