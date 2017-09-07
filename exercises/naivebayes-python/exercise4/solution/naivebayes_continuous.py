from utils.files import loadCsv
from utils.dataset import split, separateByClass
from utils.stats import summarize_continuous, gaussianProbability
from utils.ml import getAccuracy
import random

class NaiveBayes():

	def _summarizeByClass(self, dataset):
		separated = separateByClass(dataset)
		summaries = {}
		for classValue, instances in separated.iteritems():
			summary = summarize_continuous(instances);
			del summary[-1]
			summaries[classValue] = summary
		return summaries

	def _calculateClassProbabilities(self, summaries, inputVector):
		probabilities = {}
		inputVector = [float(i) for i in inputVector]
		for classValue, classSummaries in summaries.iteritems():
			probabilities[classValue] = 1 # equiprobability for each class value
			for i in range(len(classSummaries)):
				mean, stdev = classSummaries[i]
				x = inputVector[i]
				probabilities[classValue] *= gaussianProbability(x, mean, stdev)
		return probabilities

	def _predict(self, summaries, inputVector):
		probabilities = self._calculateClassProbabilities(summaries, inputVector)
		bestLabel, bestProb = None, -1
		for classValue, probability in probabilities.iteritems():
			if bestLabel is None or probability > bestProb:
				bestProb = probability
				bestLabel = classValue
		return bestLabel

	def _getPredictions(self, summaries, testSet):
		predictions = []
		for i in range(len(testSet)):
			result = self._predict(summaries, testSet[i])
			predictions.append(result)
		return predictions

	def fit(self, training_data):
		self.summaries = self._summarizeByClass(training_data)

	def getPredictions(self, dataset):
		return self._getPredictions(self.summaries, dataset)
