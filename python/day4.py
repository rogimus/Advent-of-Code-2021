import sys

inp = sys.stdin.read().split("\n\n")
draws = inp[0].replace("\n","").split(",")
t = [y.split("\n") for y in  inp[1:]]
boards = []
for x in t:
    t2=[]
    for s in x:
        t2.append(s.split())
    boards.append(t2)
# better list comprehensiony way to do that??

    
maxscore = 0
is_final_loop = 0
i = 5
while maxscore==0 and i<len(draws):
    for b in boards:
        score = 0
        for r in range(0,5):
            if (set(b[r])).issubset(set(draws[0:i])):
                temp_b = set(b[0]).union(set(b[1]),set(b[2]),set(b[3]),set(b[4]))
                score = int(draws[i-1])*sum(map(int, temp_b.difference(set(draws[0:i]))))
                is_final_loop = 1
                break
        for c in range(0,5):
            tc = []
            for r in range(0,5):
                tc.append(b[r][c])
            if set(tc).issubset(set(draws[0:i])):
                temp_b = set(b[0]).union(set(b[1]),set(b[2]),set(b[3]),set(b[4]))
                score = int(draws[i-1])*sum(map(int, temp_b.difference(set(draws[0:i]))))
                is_final_loop = 1
                break
            
        maxscore = max(score,maxscore)
    i += 1
              

#part 2
minscore = sys.maxsize
boards2 = boards[:]
for i in range(len(draws)):
    for b in boards:
        
        if not (b in boards2):
            continue
        
        score = 0
        for r in range(0,5):
            if (set(b[r])).issubset(set(draws[0:i])):
                temp_b = set(b[0]).union(set(b[1]),set(b[2]),set(b[3]),set(b[4]))
                score = int(draws[i-1])*sum(map(int, temp_b.difference(set(draws[0:i]))))
                boards2.remove(b)
                break

        if score != 0 and len(boards2)>1:
            continue
        if len(boards2)==0:
            minscore = score
            break
        for c in range(0,5):
            tc = []
            for r in range(0,5):
                tc.append(b[r][c])
            if set(tc).issubset(set(draws[0:i])):
                temp_b = set(b[0]).union(set(b[1]),set(b[2]),set(b[3]),set(b[4]))
                score = int(draws[i-1])*sum(map(int, temp_b.difference(set(draws[0:i]))))
                boards2.remove(b)
                break

        # not bothering to choose from the boards that all finish at the same time
        if len(boards2) == 0:
            minscore = score
