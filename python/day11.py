import sys
from itertools import product

inp = sys.stdin.read().split("\n")[:-1]
data = []
for r in range(len(inp)):
    data.append(list(map(int, list(inp[r]))))
data.insert(0,['']*len(data[1]))
data.append(['']*len(data[1]))
for r in range(len(data)):
    data[r].insert(0,'')
    data[r].append('')

sgns = set()
sgns = sgns.union(set(product([1,0,-1],repeat=2)))
sgns.remove((0,0))

flashes = 0
count = 1
for i in range(0,1000):
    end = 1
    for r in range(len(data)):
        data[r] = list(map(lambda x : (x+1 if isinstance(x,int) else x), data[r]))
    while(end):
        end = 0
        for r in range(1,11):
            for c in range(1,11):
                if data[r][c] > 9:
                    for s in sgns:
                        if data[r+s[0]][c+s[1]]:
                            data[r+s[0]][c+s[1]] += 1
                    data[r][c] = 0
                    end = 1
                    flashes += 1

    synced = 0
    for r in range(1,11):
        for c in range(1,11):
            if data[r][c]:
                synced = 1
    if synced == 0:
        break
    count += 1

