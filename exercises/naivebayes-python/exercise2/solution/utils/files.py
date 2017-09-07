import csv

def loadCsv(filename, delimiter=';'):
	lines = csv.reader(open(filename, "rb"), delimiter=delimiter)
	header = next(lines)
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [x for x in dataset[i]]
	return header, dataset
