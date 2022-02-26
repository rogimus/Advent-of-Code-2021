import sys
from heapq import heappop, heappush, heapreplace

inp  = list(map(list,sys.stdin.read().split("\n")))[:-1]
unvisited = {}
sgns = [(-1,0),(1,0),(0,-1),(0,1)]
distances = []

for r in range(len(inp)):
    for c in range(len(inp[0])):
        unvisited[(r,c)] =  int(inp[r][c])
        heappush(distances, (10**10,(r,c)))


def djik(start):
    heappush(distances, (0,(0,0)))

    while unvisited:                
        t = heappop(distances)
        dist = t[0]
        x,y = t[1]

        if (x,y) not in unvisited:
            continue
        if (x,y) == (len(inp)-1, len(inp[0])-1):
            return dist
        # ^^ was getting messed up because the
        #target point might not be the furthest point in the graph


        for s in sgns:
            if 0 <= x+s[0] <= len(inp)-1 and 0 <= y+s[1] <= len(inp[0])-1:
                if (x+s[0],y+s[1]) in unvisited:
                    d = dist + unvisited[(x+s[0],y+s[1])]
                    heappush(distances,  (d, (x+s[0],y+s[1])))

        unvisited.pop((x,y))
    return dist

print(djik((0,0)))
