def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if str(testSet[x][-1]) == str(predictions[x]):
			correct += 1
	return correct/float(len(testSet))
