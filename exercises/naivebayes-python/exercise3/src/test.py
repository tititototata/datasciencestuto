import unittest
from naivebayes_continuous import NaiveBayes
from utils.files import loadCsv
from utils.dataset import split
from utils.ml import getAccuracy
class naivebayes_diabete_test(unittest.TestCase):

    def bayes_model_test(self, split_ratio, seed, expected_accuracy):
        filename = '/tuto/data/diabete.csv'
        model = NaiveBayes()
    	header, dataset = loadCsv(filename)
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
        self.bayes_model_test(0.67, 1, 0.7165354330708661)

    '''
    Test data: /tuto/data.diabete.csv
    Random seed: 11
    training size: 0.67%
    '''
    def test_seed_11_train_67(self):
        self.bayes_model_test(0.67, 11, 0.7401574803149606)

    '''
    Test data: /tuto/data.diabete.csv
    Random seed: 111
    training size: 0.67%
    '''
    def test_seed_111_train_67(self):
        self.bayes_model_test(0.67, 111, 0.7677165354330708)


if __name__ == '__main__':
    unittest.main()
