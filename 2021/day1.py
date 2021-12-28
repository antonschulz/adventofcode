
data = open("input.txt", "r")

# Part 1
def partone(data):
    result = -1
    prev = 0
    for line in data:
        try:
            line = int(line)
            if(line > prev):
                result += 1
            prev = line
        except: 
            pass
        prev = line
    return result


data = data.read().split("\n")
result = partone(data)
print("Part 1: ",result)

# Part 2
sums = [data[x:x+3] for x in range(0, len(data)-3, 1)]
sumlist  = []
for l in sums:
    r = 0
    for element in l: 
        try:
            r += int(element)
        except:
            pass
    sumlist.append(r)

print("\n Part 2: ", partone(sumlist))

    

