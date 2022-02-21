import sys

def getBoards(l):
    s = []  
    t = []
    for row in range(len(l)):
        test = l[row][0:2]
        if l[row][0:2] != "\n":
            t.append(l[row])
        else:
            s.append(t)    
            t = []
    s.append(t)
    return s

def checkBoard(board, l):
    for col in range(len(board[0].split())):
        t = 1
        for row in range(len(board)):
            entry = board[row].split()[col]
            if "\n" in entry:
                entry = entry[:-2]
            if entry not in l:
                t = 0
                break
        if t == 1:
            return 1
    for row in range(len(board)):
        t = 1
        for col in range(len(board[0].split())):
            entry = board[row].split()[col]
            if "\n" in entry:
                entry = entry[:-2]
            if entry not in l:
                t = 0
                break
        if t == 1:
            return 1
    return 0

def getScore(board, l):
    score = 0
    for row in range(len(board)):
        for col in range(len(board[0].split())):
            entry = board[row].split()[col]
            if "\n" in entry:
                entry = entry[:-2]
            if entry not in l:
                score = score + int(entry)
    return score

inp = list(sys.stdin)
draws = inp[0].split(",")
boards = getBoards(inp[2:])
maxscore = 0
t = 0
while t >= 0 and t < len(draws):
    for i in boards:
        if checkBoard(i, draws[:t]) == 1:
            maxscore = max(maxscore, getScore(i, draws[:t]))
    if maxscore > 0:
        print(maxscore*int(draws[t-1]))
        t = -1
    else:
        t = t+1

#part 2
board2 = boards.copy()
t = 0
minscore = 0
while t >= 0 and t < len(draws):
    tl = board2.copy()
    for i in tl:
        if checkBoard(i, draws[:t]) == 1:
            if len(board2) != 1:
                board2.remove(i)
            else:
                minscore = getScore(board2[0], draws[:t])

    if len(board2) == 1 and checkBoard(board2[0], draws[:t]) == 1:
        print(minscore*int(draws[t-1]))
        t = -1
    else:
        t = t+1



    




#print(boards)
#print(getBoards(boards))
#print(maxscore)