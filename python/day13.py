import sys

inp = sys.stdin.read().split("\n\n")
data = set()
for i in inp[0].split("\n"):
    x,y = i.split(",")
    data.add((int(x),int(y)))

folds = []
for i in inp[1].split("\n")[:-1]:
    t = i.split()[2]
    if t[0] == 'y':
        folds.append((0,int(t[2:])))      #could use queue but no point
    if t[0] == 'x':
        folds.append((int(t[2:]),0))

        
def fold(folds, data):
    for f in folds:
        data2 = data.copy()
        for p in data:
            if f[0] == 0:
                if p[1] > f[1]:
                    data2.add((p[0],2*f[1]-p[1]))
                    data2.remove(p)
            if f[1] == 0:
                if p[0] > f[0]:
                    data2.add((2*f[0]-p[0],p[1]))
                    data2.remove(p)
        data = data2
    return data

d = fold(folds[0:1],data)
print(len(d))  # part 1


def print_message(data, folds):
    x,y = 0,0
    for i in range(len(folds)-1,-1,-1):
        if folds[i][0] != 0 and x == 0:
            x = folds[i][0]
            continue
        if folds[i][1] != 0 and y == 0:
            y = folds[i][1]
            continue
        if x != 0 and y != 0:
            break

    for r in range(y+1):
        line = ""
        for c in range(x+1):
            if (c,r) in data:
                line += "#"
            else:
                line += "."
        print(line, end = "\n")

d2 = fold(folds, data)
print_message(d2, folds)     # part 2
