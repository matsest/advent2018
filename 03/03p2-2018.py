#!/usr/bin/env python

def parse_claim(line):
        splitted = line.split()
        idno = splitted[0].strip('#')
        x,y = map(int, splitted[2].strip(':').split(','))
        areax,areay = map(int, splitted[3].split('x'))
        return idno, x, y, areax, areay

def main():
    with open("input.txt",'r') as f:
        lines = f.readlines()

    w = h = 1000
    canvas = [[0 for x in range(w)] for y in range(h)]

    for line in lines:
        idno, x, y, areax, areay = parse_claim(line)

        for i in range(y,y+areay):
            for j in range(x,x+areax):
                canvas[i][j] += 1

    count = 0
    for i in range(h):
        for j in range(w):
            if canvas[i][j] >= 2:
                count += 1
    print "Count: ", count

    # Part 2
    for line in lines:
        idno, x, y, areax, areay = parse_claim(line)

        isUnique = True
        for i in range(y,y+areay):
            for j in range(x,x+areax):
                if canvas[i][j] >= 2:
                    isUnique = False
        if isUnique:
            print "Unique ID: ", idno

if __name__ == "__main__":
    main()
