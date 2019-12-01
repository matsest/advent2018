#!/usr/bin/env python

from collections import Counter

def main():
    with open("input.txt",'r') as f:
        lines = f.readlines()

    TwototCount = 0
    ThreetotCount = 0

    for line in lines:
        counts = set(Counter(line).values())
        if 2 in counts: TwototCount += 1
        if 3 in counts: ThreetotCount += 1

    print "2's: ", TwototCount
    print "3's: ", ThreetotCount
    print "Checksum: ", TwototCount * ThreetotCount

if __name__ == "__main__":
    main()
