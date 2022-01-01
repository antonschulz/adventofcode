import statistics

data = open("input.txt").read()
data = list(map(int, data.split(",")))
md = statistics.median(data)
fuel = 0
for item in data:
    fuel += abs(item-md)
print(fuel)    

md = int(sum(data)/len(data))
print(md)
fuel = 0
for item in data:
    fuel += sum(range(1,abs(item-md)+1))
print(fuel)

