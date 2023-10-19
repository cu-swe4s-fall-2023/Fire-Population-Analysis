import unittest
import random
import sys

sys.path.insert(0, '../../src')  # noqa
from my_utils import *

class TestUtils(unittest.TestCase):
    def test_get_column_positive(self):
        file_name = '../../Agrofood_co2_emission.csv'
        query_column = 0
        query_value = 'Afghanistan'
        expected_result = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997,
                           1998,
                           1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006,
                           2007,
                           2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
                           2016,
                           2017, 2018, 2019, 2020]
        result = get_column(file_name, query_column, query_value,
                            result_column=1)
        self.assertEqual(result, expected_result)

    def test_get_column_negative(self):
        file_name = '../../Agrofood_co2_emission.csv'
        query_column = 0
        query_value = 'Country that doesnt exist'
        expected_result = []
        result = get_column(file_name, query_column, query_value)
        self.assertEqual(result, expected_result)

    def test_get_column_negative_file_not_found(self):
        file_name = 'filedoesntexist.csv'
        query_column = 0
        query_value = 'Brazil'
        expected_result = []
        # result = get_column(file_name, query_column, query_value,
        # result_column=3)
        # self.assertEqual(result, expected_result)
        with self.assertRaises(FileNotFoundError):
            result = get_column(file_name, query_column, query_value,
                                result_column=3)

    def test_find_mean_negative_empty_array(self):
        data = []
        with self.assertRaises(ValueError):
            find_mean(data)

    def test_find_mean_positive(self):
        data = [1, 2, 3, 4, 5]
        result = find_mean(data)
        self.assertEqual(result, 3.0)

    def test_find_mean_positive_random(self):
        data = random.sample(range(1, 101), 5)
        expected_mean = sum(data) / len(data)
        result = find_mean(data)
        self.assertEqual(result, expected_mean)

    def test_find_median_positive_odd_len(self):
        data = [1, 1, 3]
        result = find_median(data)
        self.assertEqual(result, 1)

    def test_find_median_positive_even_len(self):
        data = sorted(random.sample(range(1, 100), 4))
        result = find_median(data)
        expected_result = (data[1] + data[2]) / 2
        self.assertEqual(result, expected_result)

    def test_find_median_negative_empty_array(self):
        data = []
        result = find_median(data)
        self.assertIsNone(result)

    def test_find_std_dev_positive(self):
        data = [1, 2, 3, 4]
        result = find_std_dev(data)
        self.assertAlmostEqual(result, 1.11803, places=5)

    def test_find_std_dev_negative_empty_array(self):
        data = []
        with self.assertRaises(ValueError):
            find_std_dev(data)

    def test_find_std_dev_postive(self):
        data = random.sample(range(1, 1000), 100)
        result = find_std_dev(data)
        self.assertGreaterEqual(result, 0)

        
        
if __name__ == '__main__':
    unittest.main()
