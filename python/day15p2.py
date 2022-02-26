import sys
from heapq import heappop, heappush, heapreplace
import time

time1 = time.perf_counter()
inp  = list(map(list,sys.stdin.read().split("\n")))[:-1]
unvisited = {}
sgns = [(-1,0),(1,0),(0,-1),(0,1)]
distances = []

for n in range(5):
    for k in range(5):
        for r in range(len(inp)):
            for c in range(len(inp[0])):
                unvisited[(n*len(inp)+r,k*len(inp[0])+c)] =  (n+k+int(inp[r][c])-1)%9 + 1
                heappush(distances, (10**10,(n*len(inp)+r,k*len(inp[0])+c)))

def djik(start):
    heappush(distances, (0,(0,0)))

    while unvisited:                
        t = heappop(distances)
        dist = t[0]
        x,y = t[1]

        if (x,y) not in unvisited:
            continue

        for s in sgns:
            if 0 <= x+s[0] <= 5*len(inp)-1 and 0 <= y+s[1] <= 5*len(inp[1])-1:
                if (x+s[0],y+s[1]) in unvisited:
                    d = dist + unvisited[(x+s[0],y+s[1])]
                    heappush(distances,  (d, (x+s[0],y+s[1])))

        unvisited.pop((x,y))
    return dist

print(djik((0,0)))
print("{}".format(time.perf_counter() - time1))
