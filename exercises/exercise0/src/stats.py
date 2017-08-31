import math

'''
returns the mean of an array of numbers
'''
def mean(numbers):
	raise NotImplementedError('mean method not implemented')

'''
returns the stddev of an array of numbers
'''
def stdev(numbers):
	raise NotImplementedError('stdev method not implemented')

'''
Calculate mean and stdev for all the columns in the provided
'''
def summarize(dataset):
	summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
	return summaries

'''
Gaussian probabilty density for x knowing the data distribution (mean and stddev)
x: the value we want to find the probabilty
mean: the mean for the variable x belongs to
stdev: standard deviation for the variable x belongs to
'''
def gaussianProbability(x, mean, stdev):
	raise NotImplementedError('gaussianProbability method not implemented')
