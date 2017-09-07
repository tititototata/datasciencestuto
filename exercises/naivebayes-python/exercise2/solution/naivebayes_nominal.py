from utils.files import loadCsv
from utils.dataset import split, separateByClass
from utils.ml import getAccuracy
import random

class NaiveBayes():

	def _increment_count(self, variable_proba_table, tgt_class, value):
		if tgt_class not in variable_proba_table:
			variable_proba_table[tgt_class] = {}
		if value not in variable_proba_table[tgt_class]:
			variable_proba_table[tgt_class][value] = 0

		variable_proba_table[tgt_class][value] +=  1

	'''
	returns
		- A set with all the values of the target
		- A table where each entry is the statistic of a a column. The statistics
		are a dictionnary where key are the target values and values are a dictionnary
		associating the variable value with the count:
		[
			{
			tgt_val1: {
				v1_val1:count,
				v1_val2:count
				,...}
			tgt=val2: {...} },
			...
		]
	'''
	def _get_count_tables(self, dataset):
		proba_table = None
		target_classes = set()
		for line in dataset:
			if (proba_table == None):
				proba_table = [None] * len(line)
			for i in range(0, len(line)-1):
				val = line[i]
				tgt_class = line[-1]
				target_classes.add(tgt_class)
				if (proba_table[i] == None):
					proba_table[i] = {}
				self._increment_count(proba_table[i], tgt_class, val)
		return target_classes, proba_table


	def _calculateClassProbabilities(self, inputVector):
		probabilities = {}
		for tgt_class in self.tgt_classes:
			probabilities[tgt_class] = 1
			for i in range(len(inputVector) - 1):
				variable_proba_table = self.proba_table[i]
				count_vect = variable_proba_table[tgt_class]
				total_count = sum(count_vect.values())
				value_count = 0
				if (inputVector[i] in count_vect):
					value_count = count_vect[inputVector[i]]
				probabilities[tgt_class] *= value_count / float(total_count)

		return probabilities

	def _predict(self, inputVector):
		probabilities = self._calculateClassProbabilities(inputVector)
		bestLabel, bestProb = None, -1
		for classValue, probability in probabilities.iteritems():
			if bestLabel is None or probability > bestProb:
				bestProb = probability
				bestLabel = classValue
		return bestLabel

	def _getPredictions(self, testSet):
		predictions = []
		for i in range(len(testSet)):
			result = self._predict(testSet[i])
			predictions.append(result)
		return predictions


	def fit(self, training_data):
		self.tgt_classes, self.proba_table = self._get_count_tables(training_data)

	def getPredictions(self, dataset):
		return self._getPredictions(dataset)
