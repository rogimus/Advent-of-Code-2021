import sys
from collections import Counter

inp1, inp2  = sys.stdin.read().split("\n\n")
template = {}
for i in inp2.split("\n")[:-1]:
    a, b = i.split(' -> ')
    template[a] = b
    
def get_pairs(inp):
    pairs = []
    for i in range(len(inp)-1):
        pairs.append(inp[i:i+2])
    return pairs

pairs = get_pairs(inp1)

for step in range(10):
    s = pairs[0][0]
    for i in range(len(pairs)):
        if template.get(pairs[i],0):
            s +=  template[pairs[i]] + pairs[i][1]
        else:
            s += pairs[i][1]
    pairs = get_pairs(s)
    
freq = Counter(s).most_common()
score = freq[0][1]-freq[-1][1]
print(score)
