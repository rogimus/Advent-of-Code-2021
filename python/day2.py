import sys 
directions = list(sys.stdin)

h, d, a = 0, 0, 0

for i in range(len(directions)):
    if directions[i][0] == 'f':
        h = h+int(directions[i][8])
        d = d+int(directions[i][8])*a
    if directions[i][0] == 'd':
        a = a+int(directions[i][5])
    if directions[i][0] == 'u':
        a = a-int(directions[i][3])

print("\n {}".format(h*d))