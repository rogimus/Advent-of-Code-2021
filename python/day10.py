import sys

inp = sys.stdin.read().split("\n")

illegal = {")": 3, "]": 57, "}": 1197, ">": 25137}
op = {"{", "[", "(", "<"}
closed = {"}", "]", ")", ">"}
rev = {"(": ")", "{": "}", "<": ">", "[": "]"}


# part 1
t = 0
part2 = []
for line in inp:
    is_illegal = 0
    l = []
    for c in line:
        if c in op:
            l.append(c)
        if c in closed:
            if c != rev[l[-1]]:
                t += illegal[c]
                is_illegal = 1
                break
            else:
                l.pop()
    if l and not is_illegal:
        part2.append(l)

# part 2
scores = []
points = {")": 1, "]": 2, "}": 3, ">": 4}
for l in part2:
    s = 0
    for c in range(len(l)):
        s = s*5 + points[rev[l[-1]]]
        l.pop()
    scores.append(s)

scores.sort()
winner = scores[int(len(scores)/2)]


