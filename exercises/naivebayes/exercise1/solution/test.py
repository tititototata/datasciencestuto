import unittest
from dataset import split, separateByClass
from ml import getAccuracy

class test_dataset(unittest.TestCase):

    def test_split_0(self):
        dataset = [[1], [2], [3], [4], [5]]
        splitRatio = 0
        train, test = split(dataset, splitRatio)
        self.assertEqual(len(train), 0)
        self.assertEqual(len(test), 5)

    def test_split_67(self):
        dataset = [[1], [2], [3], [4], [5]]
        splitRatio = 0.67
        train, test = split(dataset, splitRatio)
        self.assertEqual(len(train), 3)
        self.assertEqual(len(test), 2)

    def test_split_100(self):
        dataset = [[1], [2], [3], [4], [5]]
        splitRatio = 1
        train, test = split(dataset, splitRatio)
        self.assertEqual(len(train), 5)
        self.assertEqual(len(test), 0)

    def test_split_67_seed_25(self):
        dataset = [[1], [2], [3], [4], [5]]
        splitRatio = 0.67
        train, test = split(dataset, splitRatio, 25)
        self.assertEqual(train[0], [2])
        self.assertEqual(train[1], [5])
        self.assertEqual(train[2], [4])

    def test_separateByClass(self):
        dataset = [[1,20,1], [2,21,0], [3,22,1]]
        separated = separateByClass(dataset)
        self.assertEqual(len(separated['0']), 1)
        self.assertEqual(len(separated['1']), 2)

class test_ml(unittest.TestCase):
    def test_getAccuracy(self):
        testSet = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
        predictions = ['a', 'a', 'a']
        accuracy = getAccuracy(testSet, predictions)
        self.assertTrue((accuracy - 66.6666666667) < 0.0000001)

if __name__ == '__main__':
    unittest.main()
