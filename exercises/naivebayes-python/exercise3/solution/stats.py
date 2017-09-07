import math

def mean(numbers):
	if (len(numbers) == 0):
		raise ValueError("Can't compute mean on size 0 arrays")
	return sum(numbers)/float(len(numbers))

def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)

'''
Calculate mean and stdev for all the columns in the provided
return a list of tuples
[(mean(att1), stdev(att1)), (mean(att2), stdev(att2)), ...]

Use the zip(*dataset) built-in projection function.

'''
def summarize_continuous(dataset):
	summaries = []
	columns = zip(*dataset)
	for col in columns:
		col = [float(i) for i in col]
		summaries.append((mean(col), stdev(col)))

	''' Could be simply written using 'zip' projection function
	summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
	'''

	return summaries

'''
Gaussian probabilty density for x knowing the data distribution (mean and stddev)
x: the value we want to find the probabilty
mean: the mean for the variable x belongs to
stdev: standard deviation for the variable x belongs to
'''
def gaussianProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent
