import unittest
from naivebayes_nominal import NaiveBayes
from utils.files import loadCsv
from utils.dataset import split
from utils.ml import getAccuracy
class naivebayes_diabete_test(unittest.TestCase):

    def bayes_model_nominal_test(self, split_ratio, seed, expected_accuracy):
        filename = '/tuto/data/car.data'
        model = NaiveBayes()
    	header, dataset = loadCsv(filename, delimiter=',')
    	trainingSet, testSet = split(dataset, split_ratio, seed)
    	model.fit(trainingSet)
    	predictions = model.getPredictions(testSet)
    	accuracy = getAccuracy(testSet, predictions)
        self.assertEqual(accuracy, expected_accuracy)

    '''
    Test data: /tuto/data.diabete.csv
    Random seed: 1
    training size: 0.67%
    '''
    def test_seed_1_train_67(self):
        self.bayes_model_nominal_test(0.67, 1, 0.8228070175438597)

    '''
    Test data: /tuto/data.diabete.csv
    Random seed: 11
    training size: 0.67%
    '''
    def test_seed_11_train_67(self):
        self.bayes_model_nominal_test(0.67, 11, 0.8140350877192982)

    '''
    Test data: /tuto/data.diabete.csv
    Random seed: 111
    training size: 0.67%
    '''
    def test_seed_111_train_67(self):
        self.bayes_model_nominal_test(0.67, 111, 0.8122807017543859)


if __name__ == '__main__':
    unittest.main()
