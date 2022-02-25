import sys
from collections import Counter

inp1, inp2  = sys.stdin.read().split("\n\n")
template = {}
pairs = {}
count = {}
for i in inp2.split("\n")[:-1]:
    a, b = i.split(' -> ')
    template[a] = b
    pairs[a] = 0

count = Counter(inp1)
 
def get_pairs(inp):
    c = {}
    for i in range(len(inp)-1):
        c[inp[i:i+2]] = c.get(inp[i:i+2],0) + 1
    return c

pairs = get_pairs(inp1)
print(pairs)
print(count)
    
for i in range(40):
    pairs2 = pairs.copy() # adding elements to pairs
    for p in pairs:
        if pairs[p] > 0:
            if template.get(p,False):
                count[template[p]] = count.get(template[p],0) + pairs[p]
                pairs2[p] = pairs2[p] - pairs[p]
                pairs2[p[0]+template[p]] = pairs2.get(p[0]+template[p],0) + pairs[p]
                pairs2[template[p]+p[1]] = pairs2.get(template[p]+p[1],0) + pairs[p]

    pairs = pairs2
     
freq = Counter(count).most_common()
score = freq[0][1]-freq[-1][1]
print(score)
