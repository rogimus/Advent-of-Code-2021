import sys

digits = sys.stdin.read()
lines = digits.split("\n")

def part1(lines):
    total = 0
    for line in lines[:-1]:
        poop, face = line.split("|")
        for i in face.split():
            if len(i) in [2,3,4,7]:
                total += 1

    print(total)
