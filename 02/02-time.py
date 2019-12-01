#!/usr/bin/env python

from collections import Counter
from sets import Set
from os import sys

def main():
    input_file = sys.argv[1]
    with open(input_file,'r') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
   
        charlist = []

        for line in lines:
            charlist.append([char for char in line])

        for x in charlist:
            for y in charlist:
                compared = zip(x,y)
                simCount = 0
                simstring = ''
                for entry in compared:
                    if entry[0] == entry[1]: 
                        simCount += 1
                if simCount == (len(y) - 1):
                    print "Almost similar strings: ", ''.join(x), ''.join(y)
                    for i in range(len(y)):
                        if x[i] == y[i]:
                            simstring += x[i]
                    print "Simiar letters: ", simstring
                    sys.exit()


if __name__ == "__main__":
    main()
