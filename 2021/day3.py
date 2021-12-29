
data = open("input.txt", "r")

data = data.read().split("\n")

# part 1
numlen = len(data[0])
temp = [0] * numlen
for x in range(0, numlen):
    for number in data:
        try:
            match int(number[x]):
                case 0:
                    temp[x] -= 1
                case 1:
                    temp[x] += 1
        except:
            pass
gamma = []
eps = []
for x in temp:
    if x > 0:
        gamma.append( "1")
        eps.append( "0")
    elif x < 0:
        gamma.append( "0")
        eps.append( "1")
    elif x == 0:
        gamma.append( "1")
        eps.append( "0")


string = ""
gamma1 = int("".join(gamma), 2)
eps1 = int("".join(eps), 2)
print("Part 1: ",gamma1  * eps1)
#### part 2
def gamma(l_data, index):
    ones = 0
    zeros = 0
    for l in l_data:
        try:
            match l[index]:
                case "1":
                    ones += 1
                case "0":
                    zeros += 1
        except:
            pass
    else:
        if zeros > ones:
            return "0" 
        elif ones >= zeros:
            return "1"

def eps(l_data, index):
    x = gamma(l_data, index)
    if x == "1":
        return "0"
    else:
        return "1"

def oxy(l_data, index, function):
    result = []
    g = function(l_data, index) 
    for l in l_data:
        try:
            if(l[index] == g):
                result.append(l)
        except:
            pass
    else:
        return result

def p2(l_data, func, index):
    index += 1
    if(len(l_data) == 1):
        return l_data
    else:
        return p2(oxy(l_data, index, func), func, index)

oxygen = p2(data, gamma, -1)[0]
co = p2(data, eps, -1)[0]
print(int(oxygen, 2) * int(co, 2))
