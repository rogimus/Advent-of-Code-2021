import sys

inp = list(sys.stdin)

gamma = 0b0
epsilon = 0b0
oxyl = inp.copy()
c02 = inp.copy()
epstr = ""
gammastr = ""


# base case
k=0
for j in range(len(inp)):
    k = k + int(inp[j][0])   
t = k/len(inp)
if t >= 0.5:
        k =1
else:
    k =0
gammastr = gammastr +"{}".format(k)
if k == 1:
    epstr = epstr + "0"
else:
    epstr = epstr + "1"


# induction 
for i in range(1, len(inp[0])-1):
    k = 0
    for j in range(len(inp)):
        k = k + int(inp[j][i])
    t = k/len(inp)
    if t >= 0.5:
        k =1            
    elif t<0.5:
        k=0 

    #gamma = ((gamma << 1) + k)
    gammastr = gammastr+"{}".format(k)
    if k == 1:
        #epsilon = ((epsilon << 1) + 0)
        epstr = epstr + "0"
    else:
        #epsilon = ((epsilon << 1) + 1)
        epstr = epstr + "1"

#get oxygen and c02 readings
for chars in range(len(gammastr)):
    a = 0
    for j in range(len(oxyl)):
        a = a + int(oxyl[j][chars])
    ta = int(a/len(oxyl)*10)
    if ta >= 5:
        t = oxyl.copy()
        for l in t:
            if l[chars] == "0" and len(oxyl) != 1:
#                print(l)
                oxyl.remove(l)
    elif ta < 5:
        t = oxyl.copy()
        for l in t:
            if l[chars] == "1" and len(oxyl) != 1:
                oxyl.remove(l)
    b = 0
    for j in range(len(c02)):
        b = b + int(c02[j][chars])
    tb = int(b/len(c02)*10)
    if tb >= 5:
        t = c02.copy()
        for lines in t:
            if lines[chars] == "1" and len(c02) != 1:
                c02.remove(lines)
                if len(c02)==1:
                    break
    elif tb < 5:
        t = c02.copy()
        for lines in t:
            if lines[chars] == "0" and len(c02) != 1:
                c02.remove(lines)

def strtobin(s):
    k = 0b0
    for i in s:
        if i == "1":
            k = (k << 1) + 1
        elif i == "0":
            k = (k<<1)+ 0 
        #else:
            #exception
    return k

print("\n {} \n".format(gamma))
print(int(strtobin(gammastr)*strtobin(epstr)))
print(int(strtobin(oxyl[0][:-1])*strtobin(c02[0][:-1])))