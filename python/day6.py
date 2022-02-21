import sys

fish = [int(x) for x in list(sys.stdin)[0].strip("\n").split(",")]
count = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
for f in fish:
    count[f] += 1

def model(count,l):
    fishies = count.copy()
    for i in range(0,l):
        t_1 = fishies[8]
        for j in range(8,0,-1):
            t_2 = fishies[j-1]
            fishies[j-1] = t_1
            t_1 = t_2
        fishies[6] += t_2
        fishies[8] = t_2

    n = 0
    for j in fishies:
        n += fishies[j]
    return n

print(model(count, 80))  #part1
print(model(count,256))  #part2
