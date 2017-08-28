import unittest
from dataset import split, separateByClass
from stats import mean, stdev, summarize, gaussianProbability

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

    def test_separateByClass(self):
        dataset = [[1,20,1], [2,21,0], [3,22,1]]
        separated = separateByClass(dataset)
        self.assertEqual(len(separated['0']), 1)
        self.assertEqual(len(separated['1']), 2)

class test_stats(unittest.TestCase):
    def test_mean(self):
        numbers = [1,2,3,4,5]
        self.assertEqual(mean(numbers), 3.0)

    def test_stdev(self):
        numbers = [1,2,3,4,5]
        self.assertTrue((stdev(numbers) - 1.58113883008) <= 0.00001 )

    def test_summarize(self):
        dataset = [[1,20,0], [2,21,1], [3,22,0]]
        summary = summarize(dataset)
        self.assertEqual(summary[0][0], 2.0)
        self.assertEqual(summary[0][1], 1.0)
        self.assertEqual(summary[1][0], 21.0)
        self.assertEqual(summary[1][1], 1.0)

    def test_calculateProbability(self):
        proba = gaussianProbability(71.5, 73, 6.2)
        self.assertTrue((proba - 0.0624896575937) < 0.0000001)

if __name__ == '__main__':
    unittest.main()
