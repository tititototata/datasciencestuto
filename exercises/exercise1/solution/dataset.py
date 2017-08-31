import random
def split(dataset, splitRatio, seed=None):
	random.seed(seed)
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))


	return trainSet, copy

def separateByClass(dataset):
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		class_key = str(vector[-1])
		if (class_key not in separated):
			separated[class_key] = []
		separated[class_key].append(vector)
	return separated
