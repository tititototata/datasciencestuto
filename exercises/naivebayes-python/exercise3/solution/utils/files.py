import csv

def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"), delimiter=';')
	header = next(lines)
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [x for x in dataset[i]]
	return header, dataset
