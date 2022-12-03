import re
data = [x.strip() for x in open('input.txt').readlines()]
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
values = [x for x in range(1,27)]
values += [x for x in range(27,53)]

def part1():
    sum, currentSum = 0,0
    for line in data:
        mid = int(len(line)/2)
        firsthalf = line[:mid]
        secondhalf = line[mid:]
        x = dict(zip(letters, [False]*len(letters)))
        for y,z in enumerate(firsthalf):
            x[z] = True
        for y,z in enumerate(secondhalf):
            if x[z]:
                # get index of z in list x and print it
                sum += values[letters.index(z)]
                break
            
    print(sum)

def part2():
    sum = 0
    arr = [False]*len(letters)*3
    x = [data[i:i+3] for i in range(0, len(data), 3)]
    for elem in x:
        arr = [False]*len(letters)*3
        for depth, item in enumerate(elem):
            for y,z in enumerate(item):
                arr[letters.index(z)+len(letters)*depth] = True
        for a in range(len(letters)):
            if arr[a]:
                if arr[a+len(letters)]:
                    if arr[a+len(letters)*2]:
                        sum += values[a]
    print(sum)





part1()
part2()
