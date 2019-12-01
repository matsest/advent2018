#!/usr/bin/env python

def main():
    with open("input.txt",'r') as f:
        lines = f.readlines()

    w = h = 1000
    canvas = [[0 for x in range(w)] for y in range(h)]

    for line in lines:
        splitted = line.split()
        idno = splitted[0].strip('#')
        x,y = map(int, splitted[2].strip(':').split(','))
        areax,areay = map(int, splitted[3].split('x'))
        #print idno, x, y, areax, areay

        for i in range(x,x+areax):
            for j in range(y,y+areay):
                canvas[i][j] += 1

    count = 0

    for i in range(w):
        for j in range(h):
            if canvas[i][j] >= 2:
                count += 1
    print "Count: ", count

if __name__ == "__main__":
    main()
