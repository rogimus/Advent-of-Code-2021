import sys
inp = list(sys.stdin)

#part1
points = {}
for line in inp:
    p1, p2 = line.split("->")
    x1, y1 = map(int, p1.split(","))
    x2, y2 = map(int, p2.split(","))
    if x1 == x2:
        for i in range(min(y1,y2),max(y1,y2)+1):
            points[(x1,i)] = points.get((x1,i),0)+ 1

    elif y1 == y2:
        for i in range(min(x1,x2),max(x1,x2)+1):
            points[(i,y1)] = points.get((i,y1),0) + 1
#part2 
    else:
        if x1>x2:
            x=-1
        else:
            x=1
        if y1>y2:
            y=-1
        else:
            y=1
        for i in range(0,max(y1,y2)+1-min(y1,y2)):
                points[(x1+i*x,y1+i*y)] = points.get((x1+i*x,y1+i*y),0)+ 1


n = 0
for pt in points:
    if points[pt] > 1:
        n = n+1

print(n)