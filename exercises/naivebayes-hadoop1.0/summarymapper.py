#!/usr/bin/python

import sys

def read_input(file, separator=";"):
    for line in file:
        yield line.rstrip().split(separator)

# N * M dataset:
# N rows
# M column
def map(dataset):
    sums = None
    row_count = 0
    # O(N / nb_workers)
    for row in dataset:
        if sums == None:
            sums = [0] * len(row)
        try:
            for i in range(0, len(row)):
                sums[i] = sums[i] + float(row[i])
            row_count += 1
        except ValueError:
            pass
    return sums, row_count

def main():
    dataset = read_input(sys.stdin)
    # O(M)
    sums, row_count = map(dataset)
    for i in range(0, len(sums)):
        print '\t'.join([str(i), str(sums[i]), str(row_count)])

if __name__ == "__main__":
    main()
