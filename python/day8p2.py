import sys

digits = sys.stdin.read()
lines = digits.split("\n")

total = 0
for line in lines[:-1]:
    values = []
    key, digs = line.split("|")

    for i in digs.split():
        values.append(set(x for x in i))
    for i in key.split():
        values.append(set(x for x in i))

    v1 =  v7 = v4 = v8 = v9 = v6 = v0 = v3 = v5 = v2 = {}
    for i in values:
        if len(i) == 2:
            v1 = i
        if len(i) == 3:
            v7 = i
        if len(i) == 4:
            v4 = i
        if len(i)  == 7:
            v8 = i


    for i in values:
        if len(i) == 6:
            if len(i.intersection(v4)) == 4:
                v9 = i
            elif len(i.intersection(v1)) == 2:
                v0 = i
            else:
                v6 = i

    for i in values:
        if len(i) == 5:
            if len(i.intersection(v1)) == 2:
                v3 = i
            elif len(i.intersection(v4)) == 3:
                v5 = i
            else:
                v2 = i

    i = 1000
    for j in map(set,map(list,digs.split())):
        if j  == v0:
            i = i/10
            continue
        if j == v1:
            total += 1*i
            i = i/10
            continue
        if j == v2:
            total += 2*i
            i = i/10
            continue
        if j == v3:
            total += 3*i
            i = i/10
            continue
        if j == v4:
            total += 4*i
            i = i/10
            continue
        if j == v5:
            total += 5*i
            i = i/10
            continue
        if j == v6:
            total += 6*i
            i = i/10
            continue
        if j == v7:
            total += 7*i
            i = i/10
            continue
        if j == v8:
            total += 8*i
            i = i/10
            continue
        if j == v9:
            total += 9*i
            i = i/10
            continue
