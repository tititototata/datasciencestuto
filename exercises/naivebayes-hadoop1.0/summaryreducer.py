#!/usr/bin/python

import sys

def read_input(file, separator="\t"):
    for line in file:
        yield line.rstrip().split(separator)


def getByColSummaries(dataset):
    all_col_stats = {}
    # O(M)
    for col_name, partial_mean, count in dataset:
        partial_mean = float(partial_mean)
        count = float(count)

        if (col_name not in all_col_stats):
            col_values = (0, 0)
        else:
            col_values = all_col_stats[col_name]

        col_values = (col_values[0] + partial_mean, col_values[1] + count)
        all_col_stats[col_name] = col_values
    return all_col_stats

def reduce(dataset):
    all_col_stats = getByColSummaries(dataset)
    all_col_means = {}
    # O(M)
    for col_name in all_col_stats:
        col_values = all_col_stats[col_name]
        mean = float(col_values[0]) / float(col_values[1])
        all_col_means[col_name] = mean
    return all_col_means


def main():
    dataset = read_input(sys.stdin)
    all_col_stats = reduce(dataset)
    # O(M)
    for col_name in all_col_stats:
        col_mean = all_col_stats[col_name]
        print '\t'.join([col_name, str(col_mean)])

if __name__ == "__main__":
    main()
