file = open("day7.txt")
inp = [int(x) for x in file.readline().strip("\n").split(",")]

minfuel = sum([abs(x-min(inp))*(abs(x-min(inp))+1)/2 for x in inp])
for i in range(min(inp)+1, max(inp)+1):
    fuel = sum([abs(x-i)*(abs(x-i)+1)/2 for x in inp])
    minfuel = min(minfuel, fuel)

print(minfuel)
