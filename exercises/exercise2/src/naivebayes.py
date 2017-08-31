from utils.files import loadCsv
from utils.dataset import split, separateByClass
from utils.stats import summarize, gaussianProbability
from utils.ml import getAccuracy
import random

class NaiveBayes():


	def fit(self, training_data):
		raise NotImplementedError('fit() method not implemented')

	def getPredictions(self, dataset):
		raise NotImplementedError('getPredictions() method not implemented')
