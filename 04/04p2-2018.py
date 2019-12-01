#!/usr/bin/env python

from collections import Counter
from collections import defaultdict
import operator

def main():
    with open("input.txt",'r') as f:
        lines = f.readlines()
        lines.sort()

    sleepcount = Counter()
    guarddict = defaultdict(lambda: defaultdict(int))

    for line in lines:
        if 'wakes' in line:
            stoptime = int(line.split()[1].rstrip(']').split(':')[1])
            #print "Stop: ", stoptime
            #print "Asleep for : ", stoptime - starttime
            for minute in range(starttime, stoptime):
                sleepcount[guard] +=1
                guarddict[guard][minute] += 1

        elif 'asleep' in line:
            starttime = int(line.split()[1].rstrip(']').split(':')[1])
            #print "Start: ", starttime
        else:
            guard= int(line.split()[3].lstrip('#'))
            #print "\nGuard: ", guard

    # Part 1
    mostsleepingguard= max(sleepcount.items(), key=lambda val: val[1])[0]
    mostsleptminute, mostsleptlength = max(guarddict[mostsleepingguard].items(), key=lambda val: val[1])
    print "Most sleeping guard: ", mostsleepingguard
    print "Slept: ", mostsleptlength, " times at minute ", mostsleptminute
    print "Answer: ", mostsleepingguard * mostsleptminute

    # Part 2
    mostfrequentminute = 0 
    maxsleeps = 0 
    mostfrequentguard = 0
    for guard in guarddict:
        times = guarddict[guard]
        minute, sleeps= max(times.items(), key = lambda t: t[1])
        if sleeps > maxsleeps:
            mostfrequentminute = minute
            mostfrequentguard = guard
            maxsleeps = sleeps
    print "Most frequent sleeping guard: ", mostfrequentguard
    print "Slept ", maxsleeps, " times at minute ", mostfrequentminute
    print "Answer: ", mostfrequentguard * mostfrequentminute

if __name__ == "__main__":
    main()
