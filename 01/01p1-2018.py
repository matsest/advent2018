#!/usr/bin/env python

def main():
    with open("input.txt",'r') as f:
        lines = f.readlines()

        frequency = 0

    for line in lines:
        frequency += int(line)

    print frequency

        

if __name__ == "__main__":
    main()
