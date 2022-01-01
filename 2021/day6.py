import re

data = open("input.txt").read()

data = list(map(int, re.findall(r'\d', data)))

def parttwo(data, m):
    state = [0] * 9
    for item in data:
        state[item] += 1
    for i in range(0,m):
        newborn = state[0]
        state = state[1:] + state[:1]
        state[6] += newborn
        state[8] = newborn
    return sum(state)






if __name__ == "__main__":
    print("partone + " , parttwo(data,80))
    print(parttwo(data, 256))
