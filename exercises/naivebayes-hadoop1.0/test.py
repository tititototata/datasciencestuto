import unittest
import summarymapper
import summaryreducer

class map_reduce_test(unittest.TestCase):
# test_data = [
#     'col1\tcol2\tcol3', # a header line may exist and should not break the mapper
#     '1\t5\t9',
#     '2\t15\t19',
#     '3\t25\t29',
# ]
    def test_mapper(self):
        test_data = [
            ['col1', 'col2', 'col3'], # a header line may exist and should not break the mapper
            [1, 5, 9],
            [2, 15, 19],
            [3, 25, 29]
        ]
        sums, row_count = summarymapper.map(test_data)
        self.assertEqual(row_count, 3)
        self.assertEqual(len(sums), 3)
        self.assertEqual(sums[0], 6)
        self.assertEqual(sums[1], 45)

    def test_reducer_first_pass(self):
        test_data = [
           ['titi', 100, 12],
           ['toto', 200, 33],
           ['tata', 300, 43],
           ['titi', 100, 12],
           ['toto', 200, 33],
           ['tata', 300, 43]
        ]
        all_col_stats = summaryreducer.getByColSummaries(test_data)
        self.assertEqual(len(all_col_stats), 3)
        self.assertEqual(all_col_stats['titi'][0], 200)
        self.assertEqual(all_col_stats['titi'][1], 24)
        self.assertEqual(all_col_stats['toto'][0], 400)
        self.assertEqual(all_col_stats['toto'][1], 66)
        self.assertEqual(all_col_stats['tata'][0], 600)
        self.assertEqual(all_col_stats['tata'][1], 86)

    def test_reducer(self):
         test_data = [
            ['titi', 100, 12],
            ['toto', 200, 33],
            ['tata', 300, 43],
            ['titi', 100, 12],
            ['toto', 200, 33],
            ['tata', 300, 43]
         ]
         all_col_means = summaryreducer.reduce(test_data)
         self.assertEqual(all_col_means['titi'], 8.3333333333333339)
         self.assertEqual(all_col_means['toto'], 6.0606060606060606)
         self.assertEqual(all_col_means['tata'], 6.9767441860465116)


if __name__ == '__main__':
    unittest.main()
