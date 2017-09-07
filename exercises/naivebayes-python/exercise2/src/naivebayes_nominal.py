from utils.files import loadCsv
from utils.dataset import split, separateByClass
from utils.ml import getAccuracy
import random

class NaiveBayes():

	def fit(self, training_data):
		raise NotImplementedError('fit() method not implemented')

	'''
	Model 'aplication' method for a naive bayes classifier working on NOMINAL columns
	only.

	returns a vector of predictions: [0, 0, 0, 1, ...]
	Assume equiprobability for each target value (Don't compute real P(C=c_i) and
	just use P(C=c_0) = P(C=c_1) = ... = 1 '''
	def getPredictions(self, dataset):
		raise NotImplementedError('getPredictions() method not implemented')
