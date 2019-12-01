#!/usr/bin/env python

import sys

def main():
    with open("input.txt",'r') as f:
        changes = [int(i) for i in f.readlines()]
        repeated_changes = changes * 200
        #repeated_changes = [-6, 3, 8, 5, -6] * 10  # should reach 5 twice
        #repeated_changes = [7, 7, -2, -7 -4] * 10  # should reach 14 twice
        frequencies = [0] * (len(repeated_changes)+1)

    for i in range(1,len(frequencies)):
        current_freq  = frequencies[i-1] + repeated_changes[i-1]
        if current_freq in frequencies:
            print "Repeated: ", current_freq
            sys.exit()
        else:
            frequencies[i] = current_freq

if __name__ == "__main__":
    main()

# Note: this takes several minutes to execute! Should use a set or similar instead of looping through the list every time
