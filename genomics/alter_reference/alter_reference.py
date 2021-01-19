#!/usr/bin/env python3

import fileinput

def main():
    last_contig = 'chrM'
    in_last_contig = False
    for line in fileinput.input():
        if line.startswith('>'):
            if in_last_contig:
                break
            if line.startswith('>' + last_contig):
                in_last_contig = True
        print(line, end='')

if __name__ == "__main__":
    main()