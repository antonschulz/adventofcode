

inp = open("input.txt").read()

def clean_input(data):
    res = []
    for line in data.splitlines():
        line = line.split("->")
        for i in range(2):
            line[i] = list(map(int, line[i].split(",")))
        res.append(line)
    return res

# [x1, y1, x2, y2]
def values(lst):
    x_one = lst[0][0]
    x_two = lst[1][0]

    y_one = lst[0][1]
    y_two = lst[1][1]
    return [x_one, y_one, x_two, y_two]

def partoneFilter(vector):
    if (vector[0] == vector[2]):
        return True, "X"
    if (vector[1] == vector [3]):
        return True, "Y"
    else:
        return False, None

def addToMatrix(matrix, val, coord):
    if coord == "X":
        for i in range(min(val[1],val[3]), max(val[1],val[3]) + 1):
            if (i not in matrix):
                matrix[i] = [val[0]]
            else:
                matrix[i].append(val[0])
    elif coord == "Y":
        for i in range(min(val[0],val[2]), max(val[0],val[2]) + 1):
            if (val[1] not in matrix):
                matrix[val[1]] = [i]
            else:
                matrix[val[1]].append(i)
    elif coord == "D":
        #part 2 needs to be implemented
        pass
    
def countCrosses(matrix):
    count = 0
    for num in matrix.keys():
        temp = []
        for xcoord in matrix[num]:
            if(temp.count(xcoord) == 1):
                count += 1
                temp.append(xcoord)
            else:
                temp.append(xcoord)
    return count

def partone(data):
    matrix = {}
    for vector in data:
        val = values(vector)
        valid, coord = partoneFilter(val)
        if(valid):
            addToMatrix(matrix, val, coord)
    count = countCrosses(matrix)
    print(count)




def main():
    data = clean_input(inp)
    partone(data)

if __name__ == "__main__":
    main()
