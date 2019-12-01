#!/usr/bin/env python

from collections import Counter
from collections import defaultdict

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

    mostsleepingguard= max(sleepcount.items(), key=lambda val: val[1])[0]
    mostsleptminute, mostsleptlength = max(guarddict[mostsleepingguard].items(), key=lambda val: val[1])
    print "Most sleeping guard: ", mostsleepingguard
    print "Slept for: ", mostsleptlength, " in minute ", mostsleptminute
    print "Answer: ", mostsleepingguard * mostsleptminute



if __name__ == "__main__":
    main()
