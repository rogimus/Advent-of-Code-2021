import sys
from collections import defaultdict

inp = sys.stdin.read().split("\n")[:-1]
data = [x.split("-") for x in inp]
adj = defaultdict(list)
for i in data:
    adj[i[0]].append(i[1])
    adj[i[1]].append(i[0])

def dfs(v, n, finish):
    if n == 'end':
        return 1

    t=0
    for i in adj[n]:
        if i != 'start' and i.islower() and i in v and not finish:
            t += dfs(v.union({i}),i, True)
        if i.islower() and i not in v:
            t += dfs(v.union({i}), i, finish)
        elif i.isupper():
            t += dfs(v,i, finish)
            
    return t

visited = {'start'}
print(dfs(visited,'start', True)) # part 1
print(dfs(visited, 'start', False)) # part 2
