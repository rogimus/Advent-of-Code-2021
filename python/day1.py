import sys
inp = list(map(int,sys.stdin))

def inc(l, inp):
    n = 0
    for i in range(len(inp)-l):
        if inp[i]< inp[i+l]:
            n = n+1
    return n

print("\n {}".format(inc(1,inp)))
print("\n {}".format(inc(3,inp)))
    
