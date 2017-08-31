import unittest
from stats import mean, stdev, summarize, gaussianProbability

class test_stats(unittest.TestCase):
    def test_mean(self):
        numbers = [1,2,3,4,5]
        self.assertEqual(mean(numbers), 3.0)

    def test_mean_size_0(self):
        numbers = []
        with self.assertRaises(ValueError):
             mean(numbers)

    def test_stdev(self):
        numbers = [1,2,3,4,5]
        self.assertTrue((stdev(numbers) - 1.58113883008) <= 0.00001 )

    def test_summarize(self):
        dataset = [[1,20], [2,21], [3,22]]
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
