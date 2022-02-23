import sys

inp = sys.stdin.read().split("\n")[:-1]
data = []
for line in inp:
    data.append([int(x) for x in list(line)])

data.insert(0,[10]*len(data[1]))
data.append([10]*len(data[1]))
for r in range(len(data)):
    data[r].insert(0,10)
    data[r].append(10)

bottoms = []
s = 0
for r in range(1,len(data)-1):
    for c in range(1,len(data[r])-1):
        t=1
        p = data[r][c]
        if data[r+1][c] <= p:
            t += 1
        if data[r-1][c] <= p:
            t += 1
        if data[r][c+1] <= p:
            t += 1
        if data[r][c-1] <= p:
            t += 1
        if t == 1:
            s += 1+p
            bottoms.append((r,c))

# part 2
# depth first search

def dfs(p, v):
    v.add(p)

    if data[p[0]+1][p[1]] < 9 and (p[0]+1,p[1]) not in v:
        v.add((p[0]+1,p[1]))
        dfs((p[0]+1,p[1]),v)
        
    if data[p[0]-1][p[1]] < 9 and (p[0]-1,p[1]) not in v:
        v.add((p[0]-1,p[1]))
        dfs((p[0]-1,p[1]),v)
        
    if data[p[0]][p[1]+1] < 9 and (p[0],p[1]+1) not in v:
        v.add((p[0],p[1]+1))
        dfs((p[0],p[1]+1),v)
        
    if data[p[0]][p[1]-1] < 9 and (p[0],p[1]-1) not in v:
        v.add((p[0],p[1]-1))
        dfs((p[0],p[1]-1),v)

    return len(v)


basins = []
for i in bottoms:
    v = set()
    basins.append(dfs(i, v))

x1  = max(basins[0], basins[1], basins[2])
x3 = min(basins[0], basins[1], basins[2])
x2 = basins[0]+ basins[1]+ basins[2] - x1 - x3

for j in range(3,len(basins)):
    i = basins[j]
    if i > x3:
        if i > x2:
            if i > x1:
                x3 = x2
                x2 = x1
                x1 = i
            else:
                x3 = x2
                x2 = i
        else:
            x3 = i
print(x1*x2*x3)
        

